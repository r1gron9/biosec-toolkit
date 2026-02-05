# biosec-toolkit User Access Options

Complete summary of how anyone can use biosec-toolkit without being a developer.

---

## Quick Reference Table

| Method | Setup Time | Cost | Internet | Best For | Link |
|--------|------------|------|----------|----------|------|
| Google Colab | 1 minute | Free | Required | Learning, no setup | [Click here](https://colab.research.google.com/github/r1gron9/biosec-toolkit/blob/main/queries/colab_notebook.ipynb) |
| Web Interface | 5 minutes | Free | Not required | Local use, offline | Run `python app.py` |
| CLI Tool | 5 minutes | Free | Not required | Batch processing | Run `python run_queries.py` |
| Jupyter Notebook | 5 minutes | Free | Not required | Interactive learning | Run `jupyter notebook` |

---

## Option 1: Google Colab (RECOMMENDED FOR BEGINNERS)

### What You Get
- Cloud-based notebook in your browser
- No installation required
- Pre-installed scientific libraries
- Free computing power
- Save results to Google Drive

### How to Start
1. Go to: https://github.com/r1gron9/biosec-toolkit
2. Click "Open In Colab" badge at top of README
3. Wait 30-60 seconds for notebook to load
4. Click first cell, hit Ctrl+Enter to run
5. Follow examples

### What You Can Do
- Generate synthetic DNA sequences
- Inject ATTATA promoter motif
- Analyze motif distribution
- Compare sequences
- Download results to Google Drive

### Requirements
- Google account (free)
- Web browser
- Internet connection

### Documentation
See: [COLAB_GUIDE.md](COLAB_GUIDE.md)

---

## Option 2: Web Interface (LOCAL, EASIEST FOR DESKTOP)

### What You Get
- Graphical user interface
- Click-and-upload interface
- No coding required
- Works offline
- Visual results

### How to Start
1. Open Command Prompt
2. Navigate to project folder
3. Run: `python app.py`
4. Open browser to: http://localhost:5000

### What You Can Do
1. **Compare Sequences** - Upload two DNA files, see differences
2. **Generate Test File** - Create custom test sequences
3. **Inject Motif** - Add ATTATA to sequences
4. **Search Promoter** - Find ATTATA in genes
5. **Analyze Distribution** - Get statistics

### Requirements
- Python 3.8+
- Windows/Mac/Linux
- No internet required

### Documentation
See: [USER_GUIDE.md](USER_GUIDE.md)

---

## Option 3: Command Line (CLI)

### What You Get
- Fast batch processing
- Automated workflow
- CSV output
- No GUI required

### How to Start
1. Open Command Prompt
2. Navigate to: `queries` folder
3. Run: `python run_queries.py`
4. View results

### What It Does
- Generates 50 test sequences
- Injects ATTATA motif
- Analyzes results
- Creates output CSV files

### Output Files
- `generated_test_motif_inject.csv` - Generated sequences
- `inject_motif_output.csv` - With motif injected
- `analysis_results.csv` - Statistics (if generated)

### Requirements
- Python 3.8+
- Windows/Mac/Linux

### Documentation
See: [queries/README.md](queries/README.md)

---

## Option 4: Jupyter Notebook (INTERACTIVE, FOR LEARNING)

### What You Get
- Step-by-step code execution
- Learn how everything works
- See outputs inline
- Edit code easily

### How to Start
1. Install Jupyter: `pip install jupyter`
2. Navigate to `queries` folder
3. Run: `jupyter notebook queries_examples.ipynb`
4. Browser opens automatically

### What You See
- 30 cells of code and explanations
- Live code execution
- Output results below each cell
- Complete workflow examples

### Requirements
- Python 3.8+
- Jupyter installed
- Windows/Mac/Linux

### Documentation
See: [queries/README.md](queries/README.md)

---

## File Upload Formats

### CSV Format
```
predicted_dna,protein_sequence
ATGATGATGATGATGATGATGATG,MMMM
GGCGGCGGCGGCGGCGGCGGCGGC,GGGG
ATGCCAATGATGATGATGATGATG,MPMMMMM
```

### FASTA Format
```
>sequence1
ATGATGATGATGATGATGATGATG
>sequence2
GGCGGCGGCGGCGGCGGCGGCGGC
>sequence3
ATGCCAATGATGATGATGATGATG
```

Example files in: `examples/` folder

---

## System Requirements

### Minimum
- Python 3.8 or higher
- 200 MB disk space
- 512 MB RAM

### Recommended
- Python 3.10+
- 1 GB disk space
- 2 GB RAM
- Modern web browser

### Optional (for specific features)
- Google account (for Colab)
- Jupyter (for interactive notebooks)

---

## Troubleshooting

### "Python not found"
Install from: https://www.python.org/downloads

### "Port 5000 already in use"
Run instead: `python app.py --port 5001`

### "Module not found"
Run: `pip install -r requirements.txt`

### Files getting stuck
Web interface: Refresh browser (Ctrl+F5)
Colab: Runtime > Restart runtime
CLI: Press Ctrl+C and run again

---

## Feature Comparison

| Feature | Colab | Web | CLI | Jupyter |
|---------|-------|-----|-----|---------|
| No setup | Yes | No | No | No |
| GUI | No | Yes | No | No |
| Learning | Good | Fair | Poor | Excellent |
| Speed | Medium | Fast | Very Fast | Medium |
| Offline | No | Yes | Yes | Yes |
| Save to Drive | Yes | No | No | No |
| Batch processing | No | No | Yes | No |
| Customizable | No | No | Yes | Yes |

---

## Getting Help

1. Read documentation file for your chosen method
2. Check examples in `examples/` folder
3. Review error messages - they're usually clear
4. Visit GitHub: https://github.com/r1gron9/biosec-toolkit
5. Check test results: `python -m unittest discover tests/ -v`

---

## Next Steps

### First Time User?
Start with Google Colab - it's the easiest!

### Want GUI?
Use Web Interface - no coding needed.

### Processing large files?
Use Jupyter Notebook or CLI - faster.

### Learning how it works?
Use Jupyter Notebook - see everything step-by-step.

---

## Documentation Files

- **README.md** - Main documentation and technical info
- **USER_GUIDE.md** - For non-technical users
- **COLAB_GUIDE.md** - Complete Google Colab instructions
- **queries/README.md** - Module and CLI documentation
- **tests/README.md** - Test suite information

---

## File Structure

```
biosec-toolkit/
|-- app.py              (Flask web application)
|-- requirements.txt    (Python dependencies)
|-- README.md          (You are here)
|-- USER_GUIDE.md      (Non-developer guide)
|-- COLAB_GUIDE.md     (Colab instructions)
|-- USER_ACCESS.md     (This file)
|
|-- modules/           (Core functionality)
|-- queries/           (CLI and Jupyter)
|-- templates/         (Web interface)
|-- static/            (Web styling)
|-- tests/             (27 unit tests)
|-- examples/          (Sample data)
```

---

## Support & Feedback

All methods tested and working:
- 27 unit tests all passing
- Colab notebook fully functional
- Web interface responsive
- CLI fast and reliable
- Jupyter notebook interactive

For issues or suggestions: Visit GitHub repository
