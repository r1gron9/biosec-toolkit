# Google Colab Guide

## What is Google Colab?

Google Colab (Colaboratory) is a free cloud-based notebook environment that runs in your browser. No installation required!

### Benefits
- Free computing power
- Pre-installed libraries
- Save results to Google Drive
- Share notebooks with others
- No configuration needed
- Works on Windows, Mac, Linux

---

## How to Use biosec-toolkit on Colab

### Option 1: Click the Badge (Easiest)
1. Go to GitHub: https://github.com/r1gron9/biosec-toolkit
2. Click the **"Open In Colab"** badge at the top
3. Wait for notebook to load (30-60 seconds)
4. Start running code cells!

### Option 2: Manual Import to Colab
1. Go to: https://colab.research.google.com
2. Click **"File" → "Open notebook"**
3. Click **"GitHub"** tab
4. Search: `r1gron9/biosec-toolkit`
5. Select `queries/colab_notebook.ipynb`
6. Click the notebook to open

### Option 3: Upload Notebook
1. Download `queries/colab_notebook.ipynb` from GitHub
2. Go to: https://colab.research.google.com
3. Drag and drop the file into Colab
4. Click "Upload" when prompted

---

## Using the Notebook

### First Cell (IMPORTANT!)
Run the first cell - it installs required packages:
```python
# This will:
# 1. Detect you're in Colab
# 2. Install biopython and tqdm
# 3. Clone the biosec-toolkit repository
# 4. Set up the environment
```

This only needs to run once per session.

### Running Examples
Each example section has:
- **Markdown cells** - Explanations
- **Code cells** - Executable code
- **Output** - Results below code

Just click "▶" button to run a cell, or press **Ctrl+Enter**

### Working with Your Data

#### Upload Files
```
Left sidebar → "Files" icon → "Upload to session" → Choose CSV/FASTA
```

#### Download Results
```
Left sidebar → "Files" icon → Right-click file → "Download"
```

#### Save to Google Drive
```python
from google.colab import files
files.download("filename.csv")
```

Or manually save:
```
Left sidebar → "Files" icon → Right-click file → "Add shortcut to Drive"
```

---

## Features Available in Colab Notebook

1. **Generate Synthetic Sequences** - Create test DNA sequences
2. **Inject ATTATA Motif** - Insert promoter elements
3. **Analyze Distribution** - Calculate statistics
4. **Compare Sequences** - View differences
5. **Download Results** - Save to Google Drive

---

## Tips & Tricks

### Speed Tips
- Run cells in order (top to bottom)
- Don't re-run setup cell unnecessarily
- Use smaller datasets for quick testing (< 1000 sequences)

### Memory Tips
- Colab gives you ~12 GB RAM
- Good for most bioinformatics tasks
- If running out of memory, restart kernel: **Runtime → Restart runtime**

### Saving Work
- Colab saves automatically to a temporary location
- To save permanently: **File → Save a copy in Drive**
- Your Drive copy persists even after session ends

### Troubleshooting

**Error: Module not found**
→ Run the setup cell again

**Error: Out of memory**
→ Restart runtime: Runtime → Restart runtime

**Files not found**
→ Make sure to upload files first (left sidebar)

**Code runs slowly**
→ It's normal for first run. Subsequent runs cache results.

---

## Colab vs Local

| Feature | Colab | Local |
|---------|-------|-------|
| Setup Time | 1 minute | 5-10 minutes |
| Cost | Free | Free |
| Computing | Cloud | Your computer |
| Internet | Required | Not required |
| Data Size | < 2 GB | 10+ GB |
| Speed | Medium | Can be faster |
| Best For | Learning, sharing | Production |

---

## Common Use Cases

### Learn Codon Optimization
1. Open Colab notebook
2. Run Example 1 (Generate sequences)
3. Run Example 2 (Inject motif)
4. Run Example 4 (Compare)

### Analyze Your Data
1. Click "Upload to session"
2. Select your CSV file
3. Modify code with your filename
4. Run modified cells
5. Download results

### Teach Others
1. Run through notebook
2. Add notes
3. File → Save a copy in Drive
4. Share Drive link
5. Others can run the same code

---

## More Information

- Colab Tutorials: https://colab.research.google.com/notebooks/intro.ipynb
- GitHub Repository: https://github.com/r1gron9/biosec-toolkit
- Full Documentation: See README.md in repository

---

**Ready to start?** Click the "Open In Colab" badge in the README!
