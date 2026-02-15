# biosec-toolkit

> Codon Optimization and ATTATA Promoter Motif Injection for DNA Sequence Engineering

DNA sequence optimization through intelligent codon substitution. Insert ATTATA regulatory elements **WITHOUT** changing the protein they encode.

---

## About This Project

**biosec-toolkit** addresses a critical cyber-biosecurity vulnerability in DNA design pipelines. Codon optimization is essential for improving protein expression in synthetic biology and biotechnology, but conventional approaches focus only on forward-strand translation efficiency. This toolkit reveals that:

- Codon optimization can inadvertently introduce antisense promoter motifs on the complementary DNA strand
- 'ATTATA' motifs can be silently injected into sequences without altering the encoded protein
- Motifs can be deliberately injected for research or security testing purposes

By combining motif detection, silent injection algorithms, and genomic analysis, **biosec-toolkit** enables researchers to understand and defend against this vulnerability.

### Authors

**Elad Carmi**¹, **Roni Glikman**¹, **Yuval Dorfan**¹*

¹Faculty of Electrical Engineering, Holon Institute of Technology  
*Corresponding author: [dorfany@gmail.com]

---

## Quick Start

### Cloud (No Installation)
[**Launch in Google Colab**](https://colab.research.google.com/github/r1gron9/biosec-toolkit/blob/main/Colab_DNA_Analysis.ipynb) – Start analyzing immediately in your browser.

### Local (Clone & Run)
```bash
git clone https://github.com/r1gron9/biosec-toolkit.git
cd biosec-toolkit
py -m pip install -r requirements.txt
python app.py
```
Open browser: **http://localhost:5000**

**Note:** If `py` command doesn't work, try `python -m pip install -r requirements.txt` instead.

---

## Getting Started

### Option 1: Google Colab (Recommended - No Installation)

[**Open biosec-toolkit in Google Colab**](https://colab.research.google.com/github/r1gron9/biosec-toolkit/blob/main/Colab_DNA_Analysis.ipynb)

- No setup required
- Analyze sequences directly in your browser
- Export results as CSV

---

### Option 2: Clone & Run Locally

**Note: This local application is built for Windows environment only. If you are using macOS, Linux, or any other operating system, please use Option 1 (Google Colab) above.**

1. Clone the repository, paste the follwing commands inside windows powershall:
```bash
git clone https://github.com/r1gron9/biosec-toolkit.git
cd biosec-toolkit
```

2. Install dependencies:

**Option A** (Try this first - recommended for Windows):
```bash
py -m pip install -r requirements.txt
```

**Option B** (If Option A doesn't work):
```bash
python -m pip install -r requirements.txt
```

**Note:** On Windows, `py` is the default Python launcher. If `py` doesn't work, try `python` instead.

3. Start the application:

**Option A** (Try this first):
```bash
py app.py
```

**Option B** (If Option A doesn't work):
```bash
python app.py
```

4. Open in browser: **http://localhost:5000**

**Features:**
- Compare DNA sequences
- Generate test sequences
- Inject ATTATA motif
- Search for promoter motifs
- Analyze motif distribution

---

## Project Structure

```
biosec-toolkit/
│
├── Colab_DNA_Analysis.ipynb      # Interactive Colab notebook
├── app.py                         # Flask web application
├── requirements.txt               # Python dependencies
├── README.md                      # This file
│
├── modules/                       # Core analysis functions
│   ├── inject_motif.py           # ATTATA motif injection
│   ├── compare_sequences.py      # Sequence comparison
│   ├── search_motifs_quantity.py # Motif analysis
│   ├── search_promoter_motif.py  # Promoter search
│   └── generate_test_file.py     # Test sequence generation
│
├── templates/                     # HTML templates (Flask)
│   ├── base.html
│   ├── home.html
│   ├── compare_sequences.html
│   ├── inject_motif.html
│   ├── search_motifs_quantity.html
│   ├── search_promoter_motif.html
│   └── generate_test_file.html
│
├── static/                        # CSS styles
│   └── style.css
│
├── queries/                       # Advanced usage
│   ├── queries_examples.ipynb    # Jupyter notebook examples
│   └── run_queries.py             # CLI interface
│
└── examples/                      # Sample data
    ├── example_E-coli.fasta
    ├── example_genes_full_genome.csv
    └── example_multiple_sequences.csv
```

---

## Core Modules

| Module | Purpose |
|--------|---------|
| `inject_motif.py` | Insert ATTATA motif via codon optimization |
| `compare_sequences.py` | Compare two DNA sequences with detailed analysis |
| `search_motifs_quantity.py` | Analyze motif distribution and frequency |
| `search_promoter_motif.py` | Find motifs in promoter regions |
| `generate_test_file.py` | Create synthetic test sequences |

---

## Input Formats

### CSV Format
```csv
predicted_dna,protein_sequence
ATGATGATG,MMM
GCAGCAGCA,AAA
```

### FASTA Format
```
>sequence1
ATGCTAGCTAGC
>sequence2
GCTAGCTAGCT
```

---

## ATTATA Injection Strategies

| Case | Codons | Amino Acids | Result |
|------|--------|-------------|--------|
| 1 | ATT + ATA | Ile + Ile | ATTATA |
| 2 | GCA + TTA + TAC | Ala + Leu + Tyr | ATTATA |
| 3 | AAT + TAT + ATG | Asn + Tyr + Met | ATTATA |

---

## Requirements

- **Python** 3.8+
- **Flask** – Web framework
- **Biopython** – DNA sequence analysis
- **Pandas** – Data manipulation
- **NumPy** – Numerical operations
- **tqdm** – Progress bars

---

## Links

- **Repository:** https://github.com/r1gron9/biosec-toolkit
- **Live Demo (Colab):** [Open Notebook](https://colab.research.google.com/github/r1gron9/biosec-toolkit/blob/main/Colab_DNA_Analysis.ipynb)
- **Web Interface:** http://localhost:5000 (after running locally)
