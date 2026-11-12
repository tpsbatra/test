import csv

# Read the orders data from the CSV file using DictReader
def read_orders(filename):
    orders = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            orders.append(row)
    return orders

# Process all orders to calculate shipped revenue, pending counts, and cancellations
def process_orders(orders):
    warehouse_revenue = {}
    warehouse_pending = {}
    cancelled_count = 0
    
    for order in orders:
        warehouse = order['warehouse']
        status = order['status']
        
        if warehouse not in warehouse_revenue:
            warehouse_revenue[warehouse] = 0.0
        if warehouse not in warehouse_pending:
            warehouse_pending[warehouse] = 0
            
        if status == 'Shipped':
            revenue = float(order['quantity']) * float(order['unit_price'])
            warehouse_revenue[warehouse] += revenue
        elif status == 'Pending':
            warehouse_pending[warehouse] += 1
        elif status == 'Cancelled':
            cancelled_count += 1
            
    return warehouse_revenue, warehouse_pending, cancelled_count

# Build the required summary lines sorted alphabetically by warehouse
def create_summary_lines(warehouse_revenue, warehouse_pending, cancelled_count):
    lines = []
    
    # Add the header for shipped revenue
    lines.append("Shipped revenue by warehouse:")
    
    # Sort warehouses alphabetically
    sorted_warehouses = sorted(warehouse_revenue.keys())
    
    total_shipped_revenue = 0.0
    for wh in sorted_warehouses:
        rev = warehouse_revenue[wh]
        total_shipped_revenue += rev
        lines.append(f"{wh}: Rs {rev}")
        
    # Add the total cancelled orders count
    lines.append(f"Orders cancelled: {cancelled_count}")
    
    # Find the warehouse with the highest number of pending orders
    max_pending = -1
    max_pending_wh = ""
    for wh in sorted(warehouse_pending.keys()):
        count = warehouse_pending[wh]
        if count > max_pending:
            max_pending = count
            max_pending_wh = wh
            
    lines.append(f"Warehouse with most pending orders: {max_pending_wh} ({max_pending})")
    
    # Add the total shipped revenue sum
    lines.append(f"Total shipped revenue: Rs {total_shipped_revenue}")
    
    return lines

# Execute the complete program workflow
def main():
    # Step 1: Read the CSV file containing orders
    orders = read_orders('orders.csv')
    
    # Step 2: Compute revenue and order statuses grouped by warehouse
    warehouse_revenue, warehouse_pending, cancelled_count = process_orders(orders)
    
    # Step 3: Format the summary output lines in the specified order
    lines = create_summary_lines(warehouse_revenue, warehouse_pending, cancelled_count)
    
    # Step 4: Print each summary line to the console
    for line in lines:
        print(line)
        
    # Step 5: Save the summary lines to summary.txt, one line per row
    with open('summary.txt', mode='w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

if __name__ == '__main__':
    main()