# How to Publish This Project on GitHub Pages

Follow these steps to host your Python project as a live website for free.

## Step 1: Create a Public Repository
1. Log in to your account at [github.com](https://github.com).
2. Click the **+** icon in the top-right corner and choose **New repository**.
3. Give your repository a short name (for example, `invoice-matcher`).
4. Make sure **Public** is selected.
5. Click **Create repository**.

## Step 2: Upload All Eight Files at the Top Level
Make sure all eight files are placed directly in the main folder of your repository (not inside any subfolders):
- `index.html`
- `reconcile.py`
- `vendors.csv`
- `invoices.csv`
- `payments.csv`
- `rules.json`
- `README.md`
- `PUBLISHING.md`

To upload them:
1. On your new repository page, click **uploading an existing file**.
2. Drag and drop all eight files into the upload box, or click **choose your files** to select them.
3. Wait for all eight files to finish uploading.
4. Click **Commit changes** at the bottom of the page.

## Step 3: Turn On GitHub Pages
1. At the top of your repository page, click **Settings**.
2. In the left sidebar, click **Pages**.
3. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
4. Under **Branch**, select **main** and choose **/ (root)** as the folder.
5. Click **Save**.

## Step 4: Open Your Live Website
1. Wait 1 to 2 minutes for GitHub to publish your site.
2. Refresh the **Settings > Pages** screen.
3. A box at the top will display: **Your site is live at `https://<your-username>.github.io/<repository-name>/`**.
4. Click the link to open your app.

---

## Troubleshooting

### A file is missing
- **What you see:** A red error banner saying it could not find or load one of the files (for example, `invoices.csv` or `reconcile.py`).
- **How to fix it:** Open your repository on GitHub and check that all eight files are listed at the top level with the exact spelling and lowercase names (`index.html`, `reconcile.py`, `rules.json`, `vendors.csv`, `invoices.csv`, `payments.csv`). If a file is inside a folder, move it to the root folder.

### The page shows nothing after a few seconds
- **What you see:** A blank screen, a 404 error, or the loading message never finishes.
- **How to fix it:**
  - If you see a **404 Not Found** page, wait another minute and refresh, or double-check that **main** and **/ (root)** are selected under **Settings > Pages**.
  - If the status message gets stuck, check your internet connection because the browser needs to download Python (Pyodide) the first time you open the page.
  - Note: Opening `index.html` directly by double-clicking it on your computer will not work due to browser security rules; view it through your GitHub Pages link instead.

### The results look wrong
- **What you see:** Unexpected invoice statuses, wrong totals, or a Python error message.
- **How to fix it:**
  - Open `rules.json`, `vendors.csv`, `invoices.csv`, and `payments.csv` on GitHub and check for typos, extra blank lines at the bottom, or wrong date formats (all dates must be `YYYY-MM-DD`).
  - Make sure all rupee amounts and `payment_terms_days` are whole numbers without commas or currency symbols (write `5000`, not `5,000` or `Rs 5000`).
  - Remember that `reconcile.py` checks rules in order: an unknown vendor or unpaid overdue invoice is flagged before checking payment amounts.
