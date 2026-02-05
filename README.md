# 🧬 biosec-toolkit

A comprehensive **Codon Optimization and Bioinformatics Analysis Platform** for DNA sequence engineering and ATTATA promoter motif injection while preserving protein sequences.

## 🎯 Overview

**biosec-toolkit** is a Flask-based bioinformatics tool that enables researchers to:
- **Optimize DNA sequences** through intelligent codon selection
- **Inject ATTATA promoter motifs** while maintaining exact protein functionality
- **Analyze genomic sequences** for motif distribution and patterns
- **Compare sequence variants** with detailed triplet-level analysis
- **Generate synthetic test sequences** for validation and testing

### Key Innovation
The toolkit uses **synonymous codon optimization** to insert the ATTATA motif into DNA sequences without altering the resulting protein - a critical capability for genetic engineering and synthetic biology applications.

## 🧪 Core Features

### 1. **Codon Optimization & Motif Injection**
- Inject ATTATA promoter motifs into DNA sequences
- Preserve 100% protein sequence integrity
- Three intelligent injection strategies based on codon flexibility
- Real-time genetic change tracking

### 2. **Sequence Comparison Analysis**
- Compare DNA sequences at the triplet level
- Identify differences with color-coded visualization
- Analyze reverse complement regions
- Search for regulatory motifs in complement sequences

### 3. **Promoter Motif Search**
- Search for ATTATA in gene promoter regions
- Load genomic sequences (FASTA) and gene locations (CSV)
- Calculate probability of motif occurrence
- Identify all occurrence positions

### 4. **Motif Quantity Analysis**
- Analyze ATTATA distribution in sequence databases
- Identify and report duplicate sequences
- Calculate occurrence probability at nucleotide and sequence levels
- Generate comprehensive analysis reports

### 5. **Synthetic Test Data Generation**
- Generate realistic synthetic DNA sequences
- Create sequences with multi-case ATTATA injection scenarios
- Export as CSV for testing and validation

## 📊 Technical Stack

- **Backend:** Flask (Python web framework)
- **Bioinformatics:** Biopython (Bio.Seq, codon tables)
- **Data Processing:** pandas, numpy
- **Progress Tracking:** tqdm
- **Frontend:** HTML5, CSS3, Bootstrap

## 📁 Project Structure

```
biosec-toolkit/
├── app.py                          # Flask application
├── requirements.txt                # Dependencies
├── README.md                       # This file
├── .gitignore                      # Git configuration
│
├── modules/                        # Core logic
│   ├── compare_sequences.py        # Sequence comparison
│   ├── search_promoter_motif.py    # ATTATA search in promoters
│   ├── search_motifs_quantity.py   # Motif distribution analysis
│   ├── generate_test_file.py       # Synthetic sequence generation
│   └── inject_motif.py             # ATTATA injection engine
│
├── templates/                      # Web interface
│   ├── base.html
│   ├── home.html
│   ├── compare_sequences.html
│   ├── search_promoter_motif.html
│   ├── search_motifs_quantity.html
│   ├── generate_test_file.html
│   └── inject_motif.html
│
├── static/                         # CSS and assets
│   └── style.css
│
├── examples/                       # Example data
│   ├── example_E-coli.fasta
│   ├── example_genes_full_genome.csv
│   └── example_multiple_sequences.csv
│
└── queries/                        # Query execution environment
    ├── README.md                   # Detailed query documentation
    ├── run_queries.py              # Ready-to-execute examples
    └── queries_examples.ipynb      # Interactive Jupyter notebook
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/r1gron9/biosec-toolkit.git
cd biosec-toolkit
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
Navigate to `http://localhost:5000` in your browser.

#### Command-Line Queries
```bash
cd queries
python run_queries.py
```

#### Interactive Jupyter Notebook
```bash
cd queries
jupyter notebook queries_examples.ipynb
```

## 📖 Usage Examples

### Direct Python Usage

**Example 1: Compare two sequences**
```python
from modules import compare_sequences

seq1 = "ATGCTAGCTAGC"
seq2 = "ATGCAAGCTAGC"

result = compare_sequences.display_results(
    seq1, seq2, 
    optimizer1="Version A", 
    optimizer2="Version B"
)
```

**Example 2: Inject ATTATA motif**
```python
from modules import inject_motif

results = inject_motif.process_csv(
    'input_sequences.csv',
    'optimized_output.csv'
)
print(f"Successfully optimized {results['total_sequences']} sequences")
```

**Example 3: Search for ATTATA in promoters**
```python
from modules import search_promoter_motif

results = search_promoter_motif.process_files(
    'genes.csv',
    'genome.fasta'
)
print(f"Found {results['count']} ATTATA motifs")
print(f"Probability: {results['probability']}")
```

For more examples, see [queries/README.md](queries/README.md) and [queries/queries_examples.ipynb](queries/queries_examples.ipynb)

## 📊 Input Data Formats

### Gene Locations CSV
```csv
Accession,Start,Stop,Gene_symbol,Strand,NCBI_Gene_ID,Name
NC_000001,1000,2000,GeneA,+,12345,Gene A Description
NC_000001,3000,4000,GeneB,-,12346,Gene B Description
```

### FASTA Sequences
```
>sequence_id description
ATGCTAGCTAGCTAGCTAGC
TAGCTAGCTAGCTAGCTAG
```

### Protein Database CSV
```csv
Serial,Id,predicted_dna,protein_sequence,organism_name
1,protein_001,ATGCTAGC...,MLAIV...,E.coli
2,protein_002,GCTAGCTA...,STWPQ...,S.cerevisiae
```

## 🔧 ATTATA Motif Injection Strategies

The toolkit supports three intelligent codon modification strategies:

| Case | Codons | Amino Acids | Result |
|------|--------|-------------|--------|
| **Case 1** | ATT + ATA | Ile + Ile | ATTATA |
| **Case 2** | GCA + TTA + TAC | Ala + Leu + Tyr | ATTATA |
| **Case 3** | AAT + TAT + ATG | Asn + Tyr + Met | ATTATA |

Each case uses synonymous codons to preserve the original protein while inserting the motif.

## 📈 Performance Features

- **Progress bars** for long-running operations (tqdm)
- **Optimized DataFrame operations** for large datasets
- **Batch processing** for multiple sequences
- **Efficient motif searching** using string operations

## 📝 Output Files Generated

When running analysis, the toolkit generates:
- **cleaned_database.csv** - Deduplicated sequence database
- **duplicates_report.csv** - List of identified duplicate sequences
- **inject_motif_output.csv** - Optimized sequences with injected motif
- Custom CSV files for analysis results

## 🧬 Biological Context

### ATTATA Motif
The ATTATA hexanucleotide is a transcription factor binding site found in bacterial promoter regions. It's part of the -10 box (Pribnow box) consensus sequence recognized by sigma factor in transcription initiation.

### Codon Optimization
Different codons encode the same amino acid (degeneracy of genetic code). By strategically selecting synonymous codons, we can:
- Insert regulatory sequences
- Enhance gene expression
- Improve sequence composition
- Maintain protein structure

## 🔬 Research Applications

- **Synthetic biology:** Design and testing of optimized genes
- **Gene expression studies:** Insertion of regulatory elements
- **Protein production:** Codon optimization for heterologous expression
- **Genome analysis:** Identification and quantification of regulatory motifs
- **Quality control:** Validation of genetic constructs

## 📚 Dependencies

- **Flask** - Web framework for the UI
- **Biopython** - Bioinformatics sequence handling and codon tables
- **pandas** - Data analysis and CSV operations
- **numpy** - Numerical operations
- **tqdm** - Progress bar visualization
- **Werkzeug** - File security utilities

See `requirements.txt` for specific versions.

## 🛠️ Development

### Project Structure Notes
- All core analysis logic is in `modules/` directory
- Flask routes are defined in `app.py`
- Web templates use Jinja2 templating in `templates/`
- CSS styling is in `static/style.css`

### Adding New Features
1. Create module in `modules/` for new analysis
2. Add Flask route in `app.py`
3. Create HTML template in `templates/`
4. Add example to `queries/`

## 📞 Usage Support

- Check [queries/README.md](queries/README.md) for detailed query documentation
- Run `jupyter notebook queries/queries_examples.ipynb` for interactive examples
- Examine example files in `examples/` directory
- Review source code docstrings: `help(modules.inject_motif)`

## ⚠️ Important Notes

- All protein sequences are **100% preserved** during optimization
- Large files (>10MB) may require significant processing time
- Temporary files are stored in `uploads/` directory
- The toolkit uses the standard genetic code (NCBI codon table ID 1)

## 📜 License

This project is provided as-is for bioinformatics research and educational purposes.

## 🤝 Contributing

Contributions are welcome! Areas for enhancement:
- Additional codon optimization strategies
- Support for alternative genetic codes
- Enhanced UI/UX improvements
- Performance optimizations for large datasets
- Additional motif search capabilities

---

**Last Updated:** February 2026

**Repository:** https://github.com/r1gron9/biosec-toolkit

**Questions or Issues?** Open an issue on GitHub