# DNA Sequence Analysis - Query Examples

This directory contains examples for running DNA sequence analysis queries programmatically without using the web interface.

## Quick Start

### Option 1: Jupyter Notebook (Recommended for Learning)
```bash
jupyter notebook queries_examples.ipynb
```

### Option 2: Run Python Script
```bash
python run_queries.py
```

## Available Modules

### 1. `modules.compare_sequences`
Compare two DNA sequences with detailed analysis.

**Function:** `display_results(sequence1, sequence2, optimizer1, optimizer2)`

**Returns:** HTML-formatted result string

**Example:**
```python
from modules import compare_sequences

seq1 = "ATGCTAGC"
seq2 = "ATGCAAGC"

result = compare_sequences.display_results(
    seq1, seq2,
    optimizer1="Wild-type",
    optimizer2="Mutant"
)
print(result)
```

**Features:**
- Triplet-by-triplet comparison with color coding
- Reverse complement analysis
- Motif search in reverse complement regions
- Detailed difference counting

---

### 2. `modules.search_promoter_motif`
Search for ATTATA motif in specific gene regions of a genome.

**Function:** `process_files(csv_path, fasta_path)`

**Parameters:**
- `csv_path`: Path to CSV file with gene locations
- `fasta_path`: Path to FASTA file with genomic sequence

**Returns:** Dictionary with:
- `indices`: List of positions where ATTATA was found
- `count`: Total number of occurrences
- `total_searches`: Total positions scanned
- `probability`: Calculated probability (scientific notation)

**Example:**
```python
from modules import search_promoter_motif

result = search_promoter_motif.process_files(
    'examples/example_genes_full_genome.csv',
    'examples/example_E-coli.fasta'
)

print(f"Found {result['count']} occurrences")
print(f"Probability: {result['probability']}")
print(f"First 10 indices: {result['indices'][:10]}")
```

**CSV Format Required:**
```
Accession,Start,Stop,Gene_symbol,Strand,NCBI_Gene_ID,Name
NC_000001,1000,2000,GeneA,+,123,Gene A
```

**FASTA Format Required:**
```
>sequence_header
ATGCTAGCTAGCTAGC...
```

---

### 3. `modules.search_motifs_quantity`
Analyze motif occurrences in a protein/DNA database.

**Function:** `search_motif(csv_path, motif="ATTATA")`

**Parameters:**
- `csv_path`: Path to CSV with protein database
- `motif`: DNA motif to search for (default: "ATTATA")

**Returns:** Dictionary with:
- `results_df`: HTML table of results
- `uniqueness_message`: Status of duplicate checking
- `num_sequences_with_motif`: Count of sequences containing motif
- `total_occurrences`: Total motif occurrences
- `total_nucleotides`: Total nucleotides analyzed
- `total_sequences`: Total sequences in database
- `prob_nucleotide`: Probability per nucleotide (scientific notation)
- `prob_sequence`: Probability per sequence

**Example:**
```python
from modules import search_motifs_quantity

results = search_motifs_quantity.search_motif(
    'examples/example_multiple_sequences.csv'
)

print(f"Total sequences: {results['total_sequences']}")
print(f"Sequences with motif: {results['num_sequences_with_motif']}")
print(f"Total occurrences: {results['total_occurrences']}")
print(f"Probability (nucleotide): {results['prob_nucleotide']}")
```

**CSV Format Required:**
```
Serial,Id,predicted_dna,protein_sequence,organism_name
1,prot_001,ATGCTAGC...,MLIV...,E.coli
2,prot_002,GCTAGCTA...,STWP...,S.cerevisiae
```

**Output Files Generated:**
- `cleaned_database.csv` - Deduplicated database
- `duplicates_report.csv` - List of duplicate sequences

---

### 4. `modules.generate_test_file`
Generate synthetic DNA sequences for testing.

**Function:** `generate_test_file(total_sequences, output_path)`

**Parameters:**
- `total_sequences`: Number of sequences to generate
- `output_path`: Path to save CSV file

**Example:**
```python
from modules import generate_test_file

generate_test_file.generate_test_file(
    total_sequences=100,
    output_path='my_test_data.csv'
)
```

**Generated CSV Columns:**
- `predicted_dna`: Generated DNA sequence
- `protein_sequence`: Translated protein
- `expected_case`: Expected ATTATA injection case

---

### 5. `modules.inject_motif`
Inject ATTATA motif into DNA sequences while preserving protein sequences.

**Function:** `process_csv(csv_path, output_filename)`

**Parameters:**
- `csv_path`: Path to input CSV
- `output_filename`: Path for output file

**Returns:** Dictionary with results

**Injection Strategies:**
1. **Case 1:** Two isoleucine codons (ATT + ATA → ATTATA)
2. **Case 2:** Alanine + Leucine + Tyrosine (GCA + TTA + TAC → ATTATA)
3. **Case 3:** Asparagine + Tyrosine + Methionine (AAT + TAT + ATG → ATTATA)

**Example:**
```python
from modules import inject_motif

results = inject_motif.process_csv(
    'my_test_data.csv',
    'output_with_motif.csv'
)

print(f"Total insertions: {results['total_insertions']}")
print(f"Modified sequences: {results['modified_sequences']}")
```

**Output CSV Columns:**
- `predicted_dna`: Modified DNA sequence
- `protein_sequence`: Original protein (unchanged)
- `modified_dna`: Final DNA with motif injected

---

## 🔄 Workflow Examples

### Complete Analysis Pipeline

```python
from modules import (
    generate_test_file, 
    inject_motif, 
    search_motifs_quantity
)

# Step 1: Generate test sequences
print("Generating test sequences...")
generate_test_file.generate_test_file(50, 'test_sequences.csv')

# Step 2: Inject motif into sequences
print("Injecting ATTATA motif...")
inject_motif.process_csv('test_sequences.csv', 'injected_sequences.csv')

# Step 3: Analyze motif occurrences
print("Analyzing motif distribution...")
results = search_motifs_quantity.search_motif('injected_sequences.csv')

print(f"\nResults:")
print(f"  Total sequences: {results['total_sequences']}")
print(f"  Sequences with ATTATA: {results['num_sequences_with_motif']}")
print(f"  Total occurrences: {results['total_occurrences']}")
print(f"  Probability: {results['prob_nucleotide']}")
```

### Promoter Analysis Pipeline

```python
from modules import search_promoter_motif

# Load your genome data
results = search_promoter_motif.process_files(
    'your_genes.csv',
    'your_genome.fasta'
)

# Analyze results
promoter_indices = results['indices']
total_found = results['count']
probability = results['probability']

print(f"ATTATA found in {total_found} promoter regions")
print(f"Probability of occurrence: {probability}")

# Save results to file
with open('promoter_analysis_results.txt', 'w') as f:
    f.write(f"Total ATTATA sites: {total_found}\n")
    f.write(f"Probability: {probability}\n")
    f.write(f"Indices: {', '.join(map(str, promoter_indices))}\n")
```

---

## 🧪 Testing Examples

### Test 1: Sequence Comparison
```python
from modules import compare_sequences

# Test with known sequences
test_seq1 = "ATGCTAGCTAGC"
test_seq2 = "ATGCAAGCTAGC"

result = compare_sequences.display_results(
    test_seq1, test_seq2,
    "Test A", "Test B"
)
assert "differences" in result.lower()
print("✓ Sequence comparison test passed")
```

### Test 2: Motif Search
```python
from modules import search_motifs_quantity

# Create a simple test CSV
import pandas as pd
test_data = {
    'Serial': [1, 2, 3],
    'Id': ['seq_1', 'seq_2', 'seq_3'],
    'predicted_dna': ['ATTATA', 'GCTAGC', 'ATTATAGC'],
    'protein_sequence': ['IY', 'AA', 'IYA'],
    'organism_name': ['Test', 'Test', 'Test']
}
pd.DataFrame(test_data).to_csv('test_motif.csv', index=False)

results = search_motifs_quantity.search_motif('test_motif.csv')
assert results['total_occurrences'] == '2'
print("✓ Motif search test passed")
```

---

## 📊 File I/O

### Reading Results
```python
import pandas as pd

# Read cleaned database
df_clean = pd.read_csv('cleaned_database.csv')
print(f"Cleaned database has {len(df_clean)} sequences")

# Read duplicates report
df_dupes = pd.read_csv('duplicates_report.csv')
print(f"Found {len(df_dupes)} duplicate sequences")

# Read injection results
df_injected = pd.read_csv('inject_motif_output.csv')
print(f"Modified {len(df_injected)} sequences")
```

### Writing Custom Results
```python
import json

# Save analysis results
results = {
    'motif': 'ATTATA',
    'total_found': 150,
    'probability': '1.45e-05',
    'timestamp': '2026-02-05'
}

with open('analysis_results.json', 'w') as f:
    json.dump(results, f, indent=2)
```

---

## Common Issues & Solutions

**Issue:** Module import errors
```
ModuleNotFoundError: No module named 'modules'
```
**Solution:** Make sure you're running scripts from the project root directory:
```bash
cd path/to/bio_dna_sequences
python queries/run_queries.py  # ✓ Correct
python run_queries.py           # ✗ Wrong
```

**Issue:** FASTA format error
```
IndexError when reading FASTA
```
**Solution:** Ensure FASTA file has:
- Header line starting with `>`
- Sequence on lines below

**Issue:** CSV column name errors
```
KeyError: 'predicted_dna'
```
**Solution:** Verify CSV has correct columns:
- `search_promoter_motif`: Accession, Start, Stop, Gene_symbol, Strand, NCBI_Gene_ID, Name
- `search_motifs_quantity`: Serial, Id, predicted_dna, protein_sequence, organism_name

---

## 📞 Help & Support

- Check the main [README.md](../README.md) for general project information
- Run `jupyter notebook queries_examples.ipynb` for interactive examples
- Examine example files in `examples/` directory
- Check module docstrings: `help(modules.search_promoter_motif)`

---

**Last Updated:** February 2026
