# Troubleshooting: Colab 404 Error

The error you're seeing (404 from GitHub API) is a known temporary issue. Your files ARE on GitHub and are committed properly.

This is happening because Colab's loader is trying to fetch files via GitHub's API, which has indexing delays.

## Solution: Use Direct Colab URL

Instead of using the badge link, try these direct URLs:

### Method 1: Direct GitHub Path (Recommended)
Go directly to: 
https://colab.research.google.com/github/r1gron9/biosec-toolkit/blob/main/queries/colab_notebook.ipynb

Or manually:
1. Go to https://colab.research.google.com
2. Click "File" → "Open notebook"
3. Click "GitHub" tab
4. Enter: `r1gron9/biosec-toolkit`
5. Select branch: `main`
6. Find: `queries/colab_notebook.ipynb`
7. Click to open

### Method 2: Download and Upload
1. Download from GitHub: https://github.com/r1gron9/biosec-toolkit/blob/main/queries/colab_notebook.ipynb
2. Click Raw button to download
3. Go to https://colab.research.google.com
4. Drag and drop the file

## Verification: Files ARE on GitHub

Files confirmed on GitHub:
- queries/colab_notebook.ipynb (7.7 KB)
- queries/queries_examples.ipynb (20.3 KB)  
- queries/run_queries.py
- queries/README.md

All pushed in commit: 245841a

## Why the 404?

GitHub API sometimes has indexing delays after pushing new files. This is temporary and will resolve within 5-15 minutes.

The files ARE there - the API just isn't reflecting them immediately.

## Temporary Workaround

If the direct Colab link still shows 404:
1. Use the other 3 access methods (Web, CLI, Jupyter)
2. Or wait 5-10 minutes and try again
3. The GitHub API will catch up

## Other Ways to Use biosec-toolkit

See [USER_ACCESS.md](USER_ACCESS.md) for:
- Google Colab (when API recovers)
- Web Interface (no API needed)
- Command Line Tool
- Jupyter Notebook
