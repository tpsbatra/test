import csv
import json
import datetime

# Step 1: Read the configuration rules from the rules JSON file
def load_rules():
    with open('rules.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Step 2: Read vendor master data from the vendors CSV file into a dictionary
def load_vendors():
    vendors_dict = {}
    with open('vendors.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            vendors_dict[row['vendor_id']] = {
                'vendor_name': row['vendor_name'],
                'payment_terms_days': int(row['payment_terms_days'])
            }
    return vendors_dict

# Step 3: Read payment records from the payments CSV file into a dictionary
def load_payments():
    payments_dict = {}
    with open('payments.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            payments_dict[row['invoice_id']] = {
                'payment_date': row['payment_date'],
                'amount_paid': int(row['amount_paid'])
            }
    return payments_dict

# Step 4: Read all invoice records from the invoices CSV file
def load_invoices():
    invoices_list = []
    with open('invoices.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            invoices_list.append(row)
    return sorted(invoices_list, key=lambda x: x['invoice_id'])

# Step 5: Initialize the main function to process accounts payable matching logic
def main():
    rules = load_rules()
    as_of_date_str = rules['as_of_date']
    as_of_date = datetime.date.fromisoformat(as_of_date_str)
    tolerance = int(rules['amount_tolerance_rs'])

    vendors = load_vendors()
    payments = load_payments()
    invoices = load_invoices()

    status_counts = {
        'Paid on time': 0,
        'Paid late': 0,
        'Amount mismatch': 0,
        'Unpaid overdue': 0,
        'Unpaid not yet due': 0,
        'Unknown vendor': 0
    }

    processed_invoices = []
    amount_at_risk = 0

    # Step 6: Iterate through each invoice in sorted order and apply status rules
    for inv in invoices:
        invoice_id = inv['invoice_id']
        vendor_id = inv['vendor_id']
        invoice_date = datetime.date.fromisoformat(inv['invoice_date'])
        amount = int(inv['amount'])

        # Step 7: Check Rule 1 for unknown vendors not present in vendor master data
        if vendor_id not in vendors:
            vendor_name = 'Unknown'
            due_date_str = None
            status = 'Unknown vendor'
            amount_at_risk += amount
            has_payment = invoice_id in payments
        else:
            vendor_info = vendors[vendor_id]
            vendor_name = vendor_info['vendor_name']
            terms = vendor_info['payment_terms_days']
            due_date = invoice_date + datetime.timedelta(days=terms)
            due_date_str = due_date.isoformat()

            payment = payments.get(invoice_id)
            has_payment = payment is not None

            # Step 8: Check Rule 2 for unpaid invoices based on the as-of date
            if not has_payment:
                if as_of_date > due_date:
                    status = 'Unpaid overdue'
                    amount_at_risk += amount
                else:
                    status = 'Unpaid not yet due'
            else:
                paid_amount = payment['amount_paid']
                payment_date = datetime.date.fromisoformat(payment['payment_date'])

                # Step 9: Check Rule 3 for amount mismatches exceeding the tolerance
                if abs(paid_amount - amount) > tolerance:
                    status = 'Amount mismatch'
                    amount_at_risk += amount
                else:
                    # Step 10: Check Rule 4 for timely versus late payments
                    if payment_date <= due_date:
                        status = 'Paid on time'
                    else:
                        status = 'Paid late'

        status_counts[status] += 1

        processed_invoices.append({
            'invoice_id': invoice_id,
            'vendor_id': vendor_id,
            'vendor_name': vendor_name,
            'amount': amount,
            'due_date': due_date_str,
            'paid': has_payment,
            'status': status
        })

    # Step 11: Build the final output report structure and print as a single JSON line
    output_data = {
        'as_of_date': as_of_date_str,
        'total_invoices': len(invoices),
        'counts': status_counts,
        'amount_at_risk': amount_at_risk,
        'invoices': processed_invoices
    }

    print(json.dumps(output_data))

# Step 12: Execute the main program entry point
if __name__ == '__main__':
    main()