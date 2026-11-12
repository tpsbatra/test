# Warehouse Shipment Summary

## What this page does
This project runs a Python program (`shipment_summary.py`) directly inside your web browser without needing to install Python on your computer. It reads warehouse order records from `orders.csv`, calculates shipped revenue per warehouse, counts cancelled and pending orders, displays the summary on the screen, and lets you download the generated `summary.txt` file.

## How to open it
- **Online (GitHub Pages):** Open your published GitHub Pages link in any phone or desktop web browser.
- **On your computer:** Because web browsers block pages from reading local files directly when opened via `file://`, start a simple local server inside this project folder:
  1. Open a terminal or command prompt in the folder containing these files.
  2. Run: `python -m http.server 8000`
  3. Open `http://localhost:8000` in your browser.

## How to change the data in orders.csv
1. Open `orders.csv` in any plain-text editor (like Notepad, TextEdit, or VS Code) or directly on GitHub by clicking the file and selecting the pencil (Edit) icon.
2. Keep the first header line unchanged:
   `order_id,warehouse,item,quantity,unit_price,status`
3. Add, edit, or remove order rows underneath. Make sure `status` is set to `Shipped`, `Pending`, or `Cancelled`, and `quantity` and `unit_price` are numbers.
4. Save the file and reload the web page to see the updated results.