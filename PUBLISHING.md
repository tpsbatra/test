# Publishing to GitHub Pages

Follow these steps to put your project online for free using GitHub Pages:

1. **Create a public repository:**
   - Sign in to your account at [github.com](https://github.com).
   - Click the **+** icon in the top-right corner and choose **New repository**.
   - Enter a repository name (for example, `warehouse-summary`).
   - Make sure **Public** is selected.
   - Click **Create repository**.

2. **Upload the five files at the top level:**
   - On your new repository page, click **uploading an existing file**.
   - Drag and drop all five files (`index.html`, `shipment_summary.py`, `orders.csv`, `README.md`, and `PUBLISHING.md`) directly into the upload box. Make sure they are at the top level and not inside a subfolder.
   - Scroll down, enter a short commit message (like `Add project files`), and click **Commit changes**.

3. **Enable GitHub Pages:**
   - Click the **Settings** tab near the top of your repository page.
   - In the left sidebar, click **Pages**.
   - Under **Build and deployment**, set **Source** to **Deploy from a branch**.
   - Under **Branch**, select **main** from the first dropdown and **/ (root)** from the second dropdown.
   - Click **Save**.

4. **Open your live link:**
   - Wait about 1 to 2 minutes, then refresh the **Pages** settings screen.
   - A banner will appear at the top showing your live website URL (for example, `https://your-username.github.io/warehouse-summary/`). Click it to open your project.

## Troubleshooting

- **Missing file error on the page:**
  - Check your GitHub repository file list to confirm that `index.html`, `shipment_summary.py`, and `orders.csv` are all spelled in exact lowercase letters and sit at the top level (root) of the repository, not inside a folder.

- **Changes do not appear yet:**
  - GitHub Pages usually takes 1 to 3 minutes to rebuild after you edit or upload a file.
  - Your browser may also be showing an older saved copy. Do a hard refresh (`Ctrl + Shift + R` on Windows/Linux, or `Cmd + Shift + R` on Mac) or open the link in a private/incognito window.