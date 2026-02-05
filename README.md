# Bio DNA Sequences - Analysis Tool

A comprehensive Flask-based bioinformatics tool for analyzing DNA sequences, identifying motifs, and performing sequence comparisons.

## 🧬 Features

### 1. **Compare Sequences**
- Compare two DNA sequences side-by-side
- Identify differences at each position (triplet analysis)
- Analyze reverse complements
- Search for TATAAT motif in reverse complement regions

### 2. **Search Promoter Motif (ATTATA)**
- Upload CSV file with gene locations (Start, Stop positions)
- Upload FASTA file with genomic sequence
- Search for ATTATA motif in gene regions
- Calculate probability of occurrence
- Display all found indices

### 3. **Search Motif Quantity**
- Load protein database from CSV
- Search for ATTATA motif in DNA sequences
- Identify duplicate sequences/proteins
- Calculate motif occurrence statistics
- Generate probability metrics (nucleotide and sequence level)

### 4. **Generate Test File**
- Generate synthetic DNA sequences for testing
- Create random sequences with ATTATA motif injection cases
- Export as CSV format
- Useful for validation and testing

### 5. **Inject Motif (ATTATA)**
- Inject ATTATA motif into DNA sequences while preserving protein sequences
- Support for 3 different codon modification strategies:
  - Case 1: Two isoleucine codons (ATT + ATA)
  - Case 2: Alanine + Leucine + Tyrosine (GCA + TTA + TAC)
  - Case 3: Asparagine + Tyrosine + Methionine (AAT + TAT + ATG)
- Track all genetic changes
- Generate detailed modification reports

## 📁 Project Structure

```
bio_dna_sequences/
├── app.py                      # Flask application main file
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── .gitignore                  # Git ignore rules
│
├── modules/                    # Core analysis modules
│   ├── compare_sequences.py    # Sequence comparison logic
│   ├── search_promoter_motif.py # Promoter motif search
│   ├── search_motifs_quantity.py # Motif quantity analysis
│   ├── generate_test_file.py   # Test data generation
│   └── inject_motif.py         # Motif injection functionality
│
├── templates/                  # HTML templates
│   ├── base.html               # Base template
│   ├── home.html               # Home page
│   ├── compare_sequences.html  # Comparison interface
│   ├── search_promoter_motif.html
│   ├── search_motifs_quantity.html
│   ├── generate_test_file.html
│   └── inject_motif.html
│
├── static/                     # CSS and client-side assets
│   └── style.css               # Styling
│
├── examples/                   # Example data files
│   ├── example_E-coli.fasta
│   ├── example_genes_full_genome.csv
│   └── example_multiple_sequences.csv
│
└── queries/                    # Query examples and scripts
    ├── README.md               # Usage guide for queries
    ├── run_queries.py          # Direct Python query execution
    └── queries_examples.ipynb   # Jupyter notebook with examples
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd bio_dna_sequences
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

#### Web Interface (Flask)
```bash
python app.py
```
Then open your browser and navigate to `http://localhost:5000`

#### Command-line Queries
See the [queries/README.md](queries/README.md) for detailed examples on running analyses directly from Python.

## 📚 Usage Examples

### Direct Python Usage

```python
from modules import compare_sequences, search_motifs_quantity

# Example 1: Compare two sequences
seq1 = "ATTGCTAGC"
seq2 = "ACTGCTAGC"
result = compare_sequences.display_results(
    seq1, seq2, 
    optimizer1="Optimizer A", 
    optimizer2="Optimizer B"
)
print(result)

# Example 2: Search for motif quantity in a CSV file
results = search_motifs_quantity.search_motif("path/to/data.csv")
print(f"Found {results['total_occurrences']} motif occurrences")
```

For more examples, see [queries/queries_examples.ipynb](queries/queries_examples.ipynb)

## 🔧 Dependencies

- **Flask** - Web framework
- **Biopython** - DNA/Protein sequence handling
- **pandas** - Data analysis and CSV processing
- **tqdm** - Progress bars for long-running operations

See `requirements.txt` for exact versions.

## 📊 Data Formats

### CSV Input Format (Gene Locations)
```
Accession,Start,Stop,Gene_symbol,Strand,NCBI_Gene_ID,Name
NC_000001,1000,2000,GeneA,+,12345,Gene A Description
NC_000001,3000,4000,GeneB,-,12346,Gene B Description
```

### FASTA Input Format
```
>sequence_id description
ATGCTAGCTAGCTAGCTAGC
TAGCTAGCTAGCTAGCTAG
```

### Protein Database CSV Format
```
Serial,Id,predicted_dna,protein_sequence,organism_name
1,protein_001,ATGCTAGC...,MLAIV...,E.coli
2,protein_002,GCTAGCTA...,STWPQ...,S.cerevisiae
```

## 🧪 Testing

Generate test data:
```bash
python -c "from modules import generate_test_file; generate_test_file.generate_test_file(100, 'test_data.csv')"
```

See [queries/run_queries.py](queries/run_queries.py) for more testing scenarios.

## 📝 License

This project is provided as-is for bioinformatics analysis and research purposes.

## 👨‍💻 Development

To modify the code:

1. All core logic is in `modules/` directory
2. Flask routes are defined in `app.py`
3. HTML templates are in `templates/` directory
4. Styling is in `static/style.css`

### Adding a New Feature
1. Create module in `modules/`
2. Add route to `app.py`
3. Create HTML template in `templates/`
4. Add example to `queries/`

## ⚠️ Notes

- The ATTATA motif is a common DNA binding site for certain transcription factors
- All protein sequences are preserved during motif injection using synonymous codons
- Large files may take time to process (progress bars are shown for long operations)
- Temporary files are stored in the `uploads/` directory

---

**Last Updated:** February 2026
