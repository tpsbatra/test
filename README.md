# Accounts Payable Invoice Matcher

This page checks supplier invoices against payments and highlights any invoices that need attention. It runs the Python script (`reconcile.py`) directly in your web browser.

## What the Page Shows
- **Report Date:** The cutoff date used to check whether unpaid invoices are overdue.
- **Summary Cards:**
  - **Total Invoices:** Total number of invoices checked.
  - **Paid On Time:** Invoices paid in full on or before their due date.
  - **Need Action:** Total count of invoices with an **Amount mismatch**, **Unpaid overdue**, or **Unknown vendor** status.
  - **Amount At Risk:** Total rupee value of all invoices that need action.
- **Status Filter Buttons:** Buttons to view **All** invoices or filter by a single status.
- **Invoice Table:** Every invoice with its vendor, amount, due date, payment status, and colour-coded status badge.
- **Python Code Viewer:** A collapsible section at the bottom showing the full `reconcile.py` script.

## How to Use It
1. Open the published GitHub Pages link in any web browser.
2. Wait a few seconds while Python starts up and reads the data files.
3. Review the four summary cards at the top to see what needs action.
4. Click any status button above the table to filter the list of invoices.
5. Click **View Python Code (reconcile.py)** at the bottom if you want to inspect the Python program.

## How to Change the Data
All settings and records live in four plain text files in the same folder:
- **`rules.json`**: Edit `as_of_date` (format `YYYY-MM-DD`) to change the report date, or `amount_tolerance_rs` to change the allowed rounding difference in whole rupees.
- **`vendors.csv`**: Add or update suppliers using the columns `vendor_id`, `vendor_name`, and `payment_terms_days`.
- **`invoices.csv`**: Add or update bills using the columns `invoice_id`, `vendor_id`, `invoice_date` (`YYYY-MM-DD`), and `amount` (whole rupees).
- **`payments.csv`**: Record payments using the columns `invoice_id`, `payment_date` (`YYYY-MM-DD`), and `amount_paid` (whole rupees).

After editing and saving any of these files in your GitHub repository, wait about a minute and refresh the web page to see the updated results.

## Status Rules (Checked in Order)
Each invoice gets the first status that matches:
1. **Unknown vendor:** The invoice's `vendor_id` is not listed in `vendors.csv`.
2. **Unpaid overdue:** No payment is listed in `payments.csv`, and `as_of_date` is after the due date (`invoice_date` + `payment_terms_days`).
3. **Unpaid not yet due:** No payment is listed in `payments.csv`, and `as_of_date` is on or before the due date.
4. **Amount mismatch:** The difference between `amount_paid` and the invoice `amount` is greater than `amount_tolerance_rs`.
5. **Paid on time:** A valid payment was made on or before the due date.
6. **Paid late:** A valid payment was made after the due date.
