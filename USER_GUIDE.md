# User Guide - biosec-toolkit

## For Non-Developers

This guide explains how to use biosec-toolkit without needing to write code.

## Option 1: Web Interface (Easiest)

### Starting the Application

1. Open PowerShell or Command Prompt
2. Navigate to the project folder:
```bash
cd path/to/bio_dna_sequences
```

3. Start the web server:
```bash
python app.py
```

You should see:
```
Running on http://127.0.0.1:5000
```

4. Open your web browser and go to: **http://localhost:5000**

### What You Can Do

The web interface has 5 tools:

#### 1. **Home** 
- Overview of the application
- Links to all tools

#### 2. **Compare Sequences**
- Upload two DNA sequences (CSV or text)
- See differences at the codon level
- Visual HTML report showing differences

#### 3. **Generate Test File**
- Create synthetic DNA sequences for testing
- Choose number of sequences to generate
- Download the generated file

#### 4. **Inject Motif (ATTATA)**
- Upload DNA sequences (CSV file)
- Automatically inserts ATTATA motif into the sequences
- Result preserves protein sequences (100% accuracy)
- Download modified sequences

#### 5. **Search for ATTATA Motif**
- Upload a sequence file
- Search for ATTATA promoter motif
- Get statistical analysis
- See probability calculations

#### 6. **Analyze Motif Distribution**
- Upload a protein database (CSV)
- Analyze ATTATA distribution
- Get statistics on motif frequency
- Identify duplicates

---

## Option 2: Interactive Notebook (For Learning)

Perfect for understanding how the tools work step-by-step.

### Requirements
```bash
pip install jupyter
```

### Run It
```bash
cd queries/
jupyter notebook queries_examples.ipynb
```

This opens an interactive notebook with:
- Live code examples
- Step-by-step explanations
- Complete workflows

---

## Option 3: Command-Line Interface (For Power Users)

Don't want to use the web interface? Use the CLI:

### Run It
```bash
cd queries/
python run_queries.py
```

This will:
1. Generate 50 test sequences
2. Inject ATTATA motif
3. Analyze the results
4. Display statistics

Output files created:
- `generated_test_motif_inject.csv` - Generated sequences
- `inject_motif_output.csv` - With ATTATA injected

---

## Example Files

In the `examples/` folder, you'll find sample data:

- `example_E-coli.fasta` - E.coli genome sequence
- `example_genes_full_genome.csv` - Gene database
- `example_multiple_sequences.csv` - Multiple sequences for comparison

You can use these with any of the tools above.

---

## Input File Formats

### CSV Format
```
predicted_dna,protein_sequence
ATGATGATGATGATGATGATGATG,MMMM
GGCGGCGGCGGCGGCGGCGGCGGC,GGGG
```

### FASTA Format
```
>sequence_name
ATGATGATGATGATGATGATGATG
GGCGGCGGCGGCGGCGGCGGCGGC
```

---

## Understanding Results

### Codon Optimization
When DNA is modified to include ATTATA:
- **Protein stays the same** (100% preserved)
- **DNA changes** (synonymous substitution)
- **Result**: Motif inserted without changing function

### Motif Search
Results show:
- **Count**: How many times ATTATA appears
- **Probability**: How likely to find in random sequence
- **Locations**: Where motif was found

### Analysis Reports
- **HTML reports**: Open in any web browser
- **CSV files**: Open in Excel or any spreadsheet
- **Statistics**: Probability calculations

---

## Troubleshooting

### Web server won't start
```
Port 5000 already in use?
Run: python app.py --port 5001
```

### Large files taking too long
- Notebook Jupyter is slower than CLI
- CLI is faster for big datasets
- Web interface good for smaller files

### Files not found
Make sure files are in the correct folder when uploading

---

## System Requirements

- **Python 3.8+** (comes pre-installed on most systems)
- **Modern web browser** (Chrome, Firefox, Edge, Safari)
- **No internet required** (runs locally)
- **Windows, Mac, or Linux** (all supported)

---

## Support

For technical questions or issues:

1. Check the test results: `python -m unittest discover tests/ -v`
2. Review the README.md in the project root
3. Check GitHub: https://github.com/r1gron9/biosec-toolkit

---

## Quick Start Checklist

- [ ] Python installed and working
- [ ] Opened command prompt in project folder
- [ ] Ran `python app.py`
- [ ] Opened browser to `http://localhost:5000`
- [ ] Uploaded a test file
- [ ] Downloaded results
