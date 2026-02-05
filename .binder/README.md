# Binder Configuration

This directory contains configuration for running biosec-toolkit on Binder.

## What is Binder?

Binder is a free service that launches interactive Jupyter notebooks in the cloud. No installation required!

## How It Works

1. Click the "Binder" badge in the README
2. Infrastructure is spun up in the cloud
3. Jupyter notebook opens in your browser
4. Run code cells interactively
5. Changes are temporary (not saved)

## Configuration Files

### requirements.txt
Specifies Python packages to install. Binder will install these automatically.

Current packages:
- Flask - Web framework
- Biopython - Sequence analysis
- pandas - Data processing
- numpy - Numerical computing
- tqdm - Progress bars
- jupyter - Notebook interface

### runtime.txt (Optional)
Could specify Python version explicitly if needed:
```
python-3.9
```

Currently using system default (3.10+).

## Troubleshooting

**Binder takes too long?**
- First launch can take 2-3 minutes
- Subsequent launches are faster
- Consider running locally for repeated use

**Need a specific library?**
- Add to requirements.txt
- Commit to GitHub
- Binder will install on next rebuild

**Want to save changes?**
- Download the notebook: File → Download as → .ipynb
- Upload to your own GitHub to create your own Binder link

## Documentation

For more information, visit: https://mybinder.readthedocs.io/

## Current Binder Configuration

Repository: r1gron9/biosec-toolkit
Branch: main
Path: queries/queries_examples.ipynb

Direct link:
https://mybinder.org/v2/gh/r1gron9/biosec-toolkit/main?filepath=queries/queries_examples.ipynb
