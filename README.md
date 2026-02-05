# biosec-toolkit

A comprehensive Codon Optimization and Bioinformatics Analysis Platform for DNA sequence engineering and ATTATA promoter motif injection while preserving protein sequences.

**[Simple Colab (Recommended)](https://colab.research.google.com/github/r1gron9/biosec-toolkit/blob/main/queries/colab_simple.ipynb)** | [Full Colab](https://colab.research.google.com/github/r1gron9/biosec-toolkit/blob/main/queries/colab_notebook.ipynb) | [GitHub](https://github.com/r1gron9/biosec-toolkit) | [Python 3.8+](https://www.python.org)

## Quick Start

**No Installation Needed!** Click "Simple Colab (Recommended)" above to run everything in your browser.

**See [USER_ACCESS.md](USER_ACCESS.md)** for a complete overview of all 4 ways to use biosec-toolkit.

See [COLAB_GUIDE.md](COLAB_GUIDE.md) for detailed Colab instructions.

## Overview

**biosec-toolkit** is a Flask-based bioinformatics application that enables systematic analysis and optimization of DNA sequences. The software provides computational tools for:

- DNA sequence optimization through intelligent codon selection
- ATTATA promoter motif injection while maintaining protein functionality
- Comprehensive genomic sequence analysis for motif distribution and patterns
- Comparative sequence analysis with detailed nucleotide-level assessment
- Generation of synthetic test sequences for validation studies

### Research Innovation

The toolkit implements **synonymous codon optimization** methodology to insert regulatory sequences (ATTATA motif) into DNA without altering the resulting protein product. This capability addresses a critical need in genetic engineering and synthetic biology applications where sequence optimization must maintain biological functionality.

## Core Functionality

### Sequence Optimization with Motif Injection

The primary function of this software is to optimize DNA sequences through codon substitution while inserting the ATTATA hexanucleotide motif. The system employs three distinct algorithmic strategies based on codon flexibility constraints.

Key features:
- Insertion of ATTATA promoter elements into DNA sequences
- Complete preservation of encoded protein sequences
- Three distinct injection strategies optimized for different codon contexts
- Detailed tracking of all genetic modifications

### Comparative Sequence Analysis

Provides triplet-level sequence comparison functionality with
- Position-by-position nucleotide comparison
- Analysis of reverse complement sequences
- Regulatory motif identification in complementary regions

### Promoter Region Analysis

Enables systematic search for ATTATA motifs within gene promoter regions:
- Integration of genomic sequence data (FASTA format)
- Gene location specification (CSV format)
- Statistical analysis of motif occurrence probability
- Complete positional mapping of identified sequences

### Motif Distribution Analysis

Database-wide analysis of ATTATA occurrence patterns:
- Duplicate sequence identification and reporting
- Occurrence frequency calculation at multiple biological scales
- Probability assessment for nucleotide and sequence levels
- Comprehensive analysis report generation

### Synthetic Sequence Generation

Controlled generation of test sequences:
- Realistic synthetic DNA sequence creation
- Multi-case ATTATA injection scenario simulation
- CSV export format for downstream analysis

## Technical Architecture

**Framework and Libraries**
- Backend: Flask (Python web application framework)
- Bioinformatics: Biopython (sequence processing, codon table management)
- Data Processing: pandas, NumPy
- User Interface: HTML5, CSS3

## Project Organization

```
biosec-toolkit/
├── app.py                          # Flask application entry point
├── requirements.txt                # Python dependencies
├── README.md                       # Documentation
├── .gitignore
│
├── modules/                        # Core analysis modules
│   ├── compare_sequences.py        # Sequence comparison algorithms
│   ├── search_promoter_motif.py    # Promoter region analysis
│   ├── search_motifs_quantity.py   # Distribution analysis
│   ├── generate_test_file.py       # Test data generation
│   └── inject_motif.py             # Codon optimization engine
│
├── templates/                      # Web interface templates
│   ├── base.html
│   ├── home.html
│   ├── compare_sequences.html
│   ├── search_promoter_motif.html
│   ├── search_motifs_quantity.html
│   ├── generate_test_file.html
│   └── inject_motif.html
│
├── static/                         # CSS resources
│   └── style.css
│
├── examples/                       # Reference datasets
│   ├── example_E-coli.fasta
│   ├── example_genes_full_genome.csv
│   └── example_multiple_sequences.csv
│
└── queries/                        # Command-line interface
    ├── README.md
    ├── run_queries.py
    └── queries_examples.ipynb
```

## Installation and Setup

### System Requirements
- Python 3.8 or higher
- pip package manager

### Installation Procedure

1. Clone repository:
```bash
git clone https://github.com/r1gron9/biosec-toolkit.git
cd biosec-toolkit
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Execution

**Web-Based Interface**
```bash
python app.py
```
Access application at http://localhost:5000

**Command-Line Interface**
```bash
cd queries
python run_queries.py
```

**Interactive Analysis Environment**
```bash
cd queries
jupyter notebook queries_examples.ipynb
```

## Usage and API

### Module: Sequence Comparison

```python
from modules import compare_sequences

result = compare_sequences.display_results(
    sequence1="ATGCTAGCTAGC",
    sequence2="ATGCAAGCTAGC",
    optimizer1="Reference Sequence",
    optimizer2="Test Sequence"
)
```

### Module: Motif Injection

```python
from modules import inject_motif

results = inject_motif.process_csv(
    input_path='sequences.csv',
    output_filename='optimized_sequences.csv'
)
```

### Module: Promoter Analysis

```python
from modules import search_promoter_motif

results = search_promoter_motif.process_files(
    csv_path='gene_locations.csv',
    fasta_path='genomic_sequence.fasta'
)
```

Additional examples and documentation: See queries/README.md and queries/queries_examples.ipynb

## Data Format Specifications

### Gene Location CSV
```
Accession,Start,Stop,Gene_symbol,Strand,NCBI_Gene_ID,Name
NC_000001,1000,2000,GeneA,+,12345,Gene A Description
```

### FASTA Sequence Format
```
>identifier description
ATGCTAGCTAGCTAGCTAGC
TAGCTAGCTAGCTAGCTAG
```

### Protein Sequence Database CSV
```
Serial,Id,predicted_dna,protein_sequence,organism_name
1,protein_001,ATGCTAGC...,MLAIV...,E.coli
```

## Algorithmic Methods: Motif Injection Strategies

The system implements three codon-based insertion strategies to achieve ATTATA incorporation:

| Strategy | Codon Pair | Amino Acid Translation | Resulting Sequence |
|----------|-----------|----------------------|-------------------|
| Case 1 | ATT + ATA | Isoleucine × 2 | ATTATA |
| Case 2 | GCA + TTA + TAC | Alanine, Leucine, Tyrosine | ATTATA |
| Case 3 | AAT + TAT + ATG | Asparagine, Tyrosine, Methionine | ATTATA |

Each strategy exploits codon degeneracy to maintain protein sequence invariance while inserting the target motif.

## Output Generation

The application generates the following analysis outputs:
- cleaned_database.csv - Deduplicated sequence database
- duplicates_report.csv - Identified duplicate sequences
- inject_motif_output.csv - Optimized sequences with motif insertion
- Analysis-specific output files

## Biological and Computational Context

### ATTATA Motif Significance

The ATTATA hexanucleotide sequence represents a conserved transcription factor binding site in bacterial promoter regions. Located within the -10 box (Pribnow box), this element is recognized by sigma factors during transcriptional initiation. The sequence carries functional significance in gene regulation and promoter strength determination.

### Codon Optimization Methodology

The degeneracy of the genetic code permits multiple codon combinations to specify identical amino acid sequences. This redundancy enables strategic codon selection to:

- Incorporate regulatory elements while preserving protein structure
- Optimize codon usage for specific expression systems
- Maintain protein folding properties
- Improve expression efficiency

## Research Applications

This software is applicable to multiple research domains:

**Synthetic Biology**: Design and validation of engineered genetic constructs

**Gene Expression Studies**: Systematic insertion of regulatory elements for expression modulation

**Recombinant Protein Production**: Codon optimization for heterologous expression systems

**Genomic Analysis**: Identification and quantification of regulatory sequence elements

**Quality Control**: Computational validation of genetic construct integrity

## Software Dependencies

- Flask: Web application framework
- Biopython: Bioinformatics sequence analysis and codon table management
- pandas: Data structure and analysis
- NumPy: Numerical computation
- tqdm: Progress bar visualization
- Werkzeug: WSGI utilities and file handling

## Development Notes

**Architecture**
- Modular design with independent analysis functions in modules/ directory
- RESTful Flask routes defined in app.py
- Jinja2 template system for web interface
- CSS styling in static/style.css

**Extension Guidelines**
1. Implement new analysis functionality in modules/
2. Add corresponding Flask route in app.py
3. Create web interface template in templates/
4. Document functionality in queries/ examples

## Documentation and Support

Detailed query documentation: queries/README.md
Interactive tutorials: queries/queries_examples.ipynb
Example datasets: examples/ directory

## Notes on Implementation

- Protein sequence preservation is maintained at 100% fidelity during optimization
- Processing of large datasets (>10MB) may require extended computation time
- Temporary file storage: uploads/ directory
- Genetic code implementation: NCBI standard codon table (ID 1)

## License and Academic Use

This software is provided for bioinformatics research and academic purposes.

## Related Work and References

The application implements standard molecular biology algorithms:
- Sequence comparison (Needleman-Wunsch, Smith-Waterman variants)
- Codon substitution matrices
- Statistical analysis of sequence motifs

---

**Version**: February 2026

**Repository**: https://github.com/r1gron9/biosec-toolkit

**Inquiries**: Submit issues through GitHub repository

## Core Functionality

### Sequence Optimization with Motif Injection

The primary function of this software is to optimize DNA sequences through codon substitution while inserting the ATTATA hexanucleotide motif. The system employs three distinct algorithmic strategies based on codon flexibility constraints.

Key features:
- Insertion of ATTATA promoter elements into DNA sequences
- Complete preservation of encoded protein sequences
- Three distinct injection strategies optimized for different codon contexts
- Detailed tracking of all genetic modifications

### Comparative Sequence Analysis

Provides triplet-level sequence comparison functionality with
- Position-by-position nucleotide comparison
- Analysis of reverse complement sequences
- Regulatory motif identification in complementary regions

### Promoter Region Analysis

Enables systematic search for ATTATA motifs within gene promoter regions:
- Integration of genomic sequence data (FASTA format)
- Gene location specification (CSV format)
- Statistical analysis of motif occurrence probability
- Complete positional mapping of identified sequences

### Motif Distribution Analysis

Database-wide analysis of ATTATA occurrence patterns:
- Duplicate sequence identification and reporting
- Occurrence frequency calculation at multiple biological scales
- Probability assessment for nucleotide and sequence levels
- Comprehensive analysis report generation

### Synthetic Sequence Generation

Controlled generation of test sequences:
- Realistic synthetic DNA sequence creation
- Multi-case ATTATA injection scenario simulation
- CSV export format for downstream analysis

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

## Getting Started

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

#### Cloud: Google Colab (Recommended for beginners)
Click the **"Open in Colab"** badge at the top - runs instantly in your browser with no setup!
- No installation required
- All packages pre-installed
- Save results to Google Drive
- Link: [colab_notebook.ipynb](queries/colab_notebook.ipynb)

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

### Non-Developer Users

**See [USER_GUIDE.md](USER_GUIDE.md)** for a complete guide on using biosec-toolkit without writing code:
- Web Interface walkthrough
- Step-by-step tool instructions
- File format examples
- Troubleshooting guide

## Usage Examples

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

## ATTATA Motif Injection Strategies

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

## Biological Context

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

## Dependencies

- **Flask** - Web framework for the UI
- **Biopython** - Bioinformatics sequence handling and codon tables
- **pandas** - Data analysis and CSV operations
- **numpy** - Numerical operations
- **tqdm** - Progress bar visualization
- **Werkzeug** - File security utilities

See `requirements.txt` for specific versions.

## Development

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

## Important Notes

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