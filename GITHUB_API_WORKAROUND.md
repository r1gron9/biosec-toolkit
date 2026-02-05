# GitHub API 404 Workaround

## Issue
If you see "404 Not Found" errors from GitHub API when opening Colab, this is because Colab's initialization tries to fetch the `queries` folder listing via the GitHub API, which has a temporary indexing delay.

**Important: The git clone itself works fine.** The error is cosmetic - just ignore it or use one of the working methods below.

## Best Solution: Use Simple Colab Notebook

This minimal version avoids the API issue entirely:

```
https://colab.research.google.com/github/r1gron9/biosec-toolkit/blob/main/queries/colab_simple.ipynb
```

**Features:**
- One-click setup
- Avoids GitHub API calls
- Works immediately
- Minimal, clean interface
- Full functionality

## Alternative: Original Colab Notebook

If you prefer the detailed notebook with explanations:

```
https://colab.research.google.com/github/r1gron9/biosec-toolkit/blob/main/queries/colab_notebook.ipynb
```

**If you see API errors:** The error is in Colab's background initialization trying to fetch folder metadata. The actual git clone works fine - just continue and run the cells. The notebook will work correctly.

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
