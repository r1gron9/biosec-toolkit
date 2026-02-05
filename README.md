# biosec-toolkit

Codon Optimization and ATTATA Promoter Motif Injection for DNA Sequence Engineering

**[Open in Google Colab](https://colab.research.google.com/github/r1gron9/biosec-toolkit/blob/main/queries/colab_notebook.ipynb)** | [GitHub](https://github.com/r1gron9/biosec-toolkit) | [Python 3.8+](https://www.python.org)

## What It Does

Insert ATTATA promoter motifs into DNA sequences while preserving the protein they encode.

**Key Features:**
- Optimize DNA sequences through intelligent codon substitution  
- Inject ATTATA regulatory elements WITHOUT changing the protein
- Analyze motif distribution across sequences
- Compare DNA sequences at the nucleotide level
- Generate synthetic sequences for testing

## Installation

`ash
pip install -r requirements.txt
`

## Quick Example

### Generate Sequences

`python
from modules import generate_test_file

generate_test_file.generate_test_file(total_sequences=10, output_path='demo.csv')
`

### Inject Motif

`python
from modules import inject_motif

inject_motif.process_csv('demo.csv', 'demo_modified.csv')
`

### Analyze Results

`python
from modules import search_motifs_quantity

stats = search_motifs_quantity.search_motif('demo_modified.csv', 'ATTATA')
print(stats)
`

## Usage

### Web Interface
`ash
python app.py
# Open http://localhost:5000
`

### Command Line
`ash
python queries/run_queries.py
`

### Jupyter Notebook
`ash
jupyter notebook queries/queries_examples.ipynb
`

## Core Modules

| Module | Purpose |
|--------|---------|
| compare_sequences.py | Compare two DNA sequences |
| inject_motif.py | Insert ATTATA motif via codon optimization |
| generate_test_file.py | Create synthetic test sequences |
| search_promoter_motif.py | Find motifs in promoter regions |
| search_motifs_quantity.py | Analyze motif distribution |

## Testing

`ash
python -m unittest discover tests/ -v
`

All 27 tests passing.

## License

MIT
