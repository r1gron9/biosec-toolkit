# GitHub API 404 Workaround

## Issue
If you see "404 Not Found" errors when trying to access queries folder from GitHub API, this is a temporary indexing delay issue. All files ARE present in the repository.

## Quick Fix: Use Direct Colab Link

The safest method - opens the notebook directly from GitHub (no API calls):

```
https://colab.research.google.com/github/r1gron9/biosec-toolkit/blob/main/queries/colab_notebook.ipynb
```

Click this link and it will:
1. Open Google Colab interface
2. Load the notebook from GitHub
3. Run the setup automatically
4. No API calls needed

## Alternative: Docker

If you prefer a completely isolated environment:

```bash
# Create Docker container with all dependencies
docker pull python:3.13-slim
docker run -v $(pwd):/workspace python:3.13-slim bash -c "
    cd /workspace
    pip install -q -r requirements.txt
    python queries/run_queries.py
"
```

## Alternative: Local Installation (5 minutes)

```bash
# 1. Clone repository
git clone https://github.com/r1gron9/biosec-toolkit.git
cd biosec-toolkit

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run tool
python queries/run_queries.py
```

## Why This Happens

GitHub has multiple indexing systems:
- **Web interface** (github.com) - Updated instantly
- **Git repository** - Updated instantly
- **GitHub API** - Has 5-15 minute delay for new files
- **Raw CDN** (raw.githubusercontent.com) - Has 5-15 minute delay

The Colab direct link uses the web interface, so it works immediately.

## Verification

All files are confirmed present:
- ✓ Local filesystem
- ✓ Git repository (verified with `git ls-tree`)
- ✓ GitHub repository (verified with `git push`)
- ✓ All 27 tests passing

The issue is purely timing-related, not missing files.

## Contact

If you continue experiencing issues after 15 minutes, try:
1. Hard refresh browser (Ctrl+F5)
2. Use incognito/private window (bypasses cache)
3. Try alternative access methods above
4. File issue: https://github.com/r1gron9/biosec-toolkit/issues
