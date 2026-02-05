#!/usr/bin/env python3
"""
DNA Sequence Analysis - Query Examples
Run this script to execute all analysis examples directly from Python
"""

import sys
import os

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules import (
    compare_sequences,
    search_promoter_motif,
    search_motifs_quantity,
    generate_test_file,
    inject_motif
)
import pandas as pd


def print_header(title):
    """Print a formatted header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def print_subheader(title):
    """Print a formatted subheader"""
    print(f"\n>> {title}")
    print("-" * 70)


def example_1_compare_sequences():
    """Example 1: Compare two DNA sequences"""
    print_header("EXAMPLE 1: SEQUENCE COMPARISON")
    
    seq1 = "ATGCTAGCTAGCTAGCTAGC"
    seq2 = "ATGCAAGCTAGCTAGCTAGC"
    
    print_subheader("Input Sequences")
    print(f"Sequence 1: {seq1}")
    print(f"Sequence 2: {seq2}")
    
    result = compare_sequences.display_results(
        seq1, seq2,
        optimizer1="Wild-type",
        optimizer2="Mutant"
    )
    
    print_subheader("Results")
    # Extract plain text from HTML result
    print("HTML result generated (suitable for web display)")
    print("Contains: Triplet comparison, Reverse complement analysis, Motif search")
    

def example_2_search_promoter_motif():
    """Example 2: Search for promoter motif"""
    print_header("EXAMPLE 2: PROMOTER MOTIF SEARCH (ATTATA)")
    
    csv_path = "examples/example_genes_full_genome.csv"
    fasta_path = "examples/example_E-coli.fasta"
    
    if os.path.exists(csv_path) and os.path.exists(fasta_path):
        print_subheader("Processing Files")
        print(f"CSV File: {csv_path}")
        print(f"FASTA File: {fasta_path}")
        
        result = search_promoter_motif.process_files(csv_path, fasta_path)
        
        print_subheader("Results")
        print(f"Total ATTATA occurrences found: {result['count']}")
        print(f"Probability: {result['probability']}")
        print(f"Total positions searched: {result['total_searches']}")
        print(f"Found indices (first 10): {result['indices'][:10] if result['indices'] else 'None'}")
    else:
        print_subheader("⚠️  Example Files Not Found")
        print(f"Place example files in the 'examples/' directory:")
        print(f"  - {csv_path}")
        print(f"  - {fasta_path}")


def example_3_search_motif_quantity():
    """Example 3: Search motif quantity in database"""
    print_header("EXAMPLE 3: MOTIF QUANTITY ANALYSIS")
    
    csv_path = "examples/example_multiple_sequences.csv"
    
    if os.path.exists(csv_path):
        print_subheader("Processing CSV Database")
        print(f"CSV File: {csv_path}")
        
        results = search_motifs_quantity.search_motif(csv_path)
        
        print_subheader("Results Summary")
        print(f"Total sequences analyzed: {results['total_sequences']}")
        print(f"Sequences containing ATTATA: {results['num_sequences_with_motif']}")
        print(f"Total ATTATA occurrences: {results['total_occurrences']}")
        print(f"Total nucleotides: {results['total_nucleotides']}")
        print(f"Probability per nucleotide: {results['prob_nucleotide']}")
        print(f"Probability per sequence: {results['prob_sequence']}")
        print(f"\nUniqueness Check: {results['uniqueness_message']}")
        
        # Check generated files
        print_subheader("Generated Output Files")
        if os.path.exists("cleaned_database.csv"):
            df_clean = pd.read_csv("cleaned_database.csv")
            print(f"✓ cleaned_database.csv ({len(df_clean)} sequences)")
        
        if os.path.exists("duplicates_report.csv"):
            df_dupes = pd.read_csv("duplicates_report.csv")
            if len(df_dupes) > 0:
                print(f"✓ duplicates_report.csv ({len(df_dupes)} duplicates found)")
            else:
                print(f"✓ duplicates_report.csv (No duplicates found)")
    else:
        print_subheader("⚠️  Example File Not Found")
        print(f"Place example file in 'examples/' directory:")
        print(f"  - {csv_path}")


def example_4_generate_test_file():
    """Example 4: Generate synthetic test sequences"""
    print_header("EXAMPLE 4: GENERATE TEST FILE")
    
    output_path = "generated_test_sequences.csv"
    num_sequences = 50
    
    print_subheader("Generating Test Data")
    print(f"Generating {num_sequences} synthetic DNA sequences...")
    
    generate_test_file.generate_test_file(num_sequences, output_path)
    
    print_subheader("Results")
    if os.path.exists(output_path):
        df = pd.read_csv(output_path)
        print(f"✓ Generated {len(df)} sequences")
        print(f"✓ Saved to: {output_path}")
        print(f"\nColumns: {', '.join(df.columns.tolist())}")
        print(f"\nFirst sequence:")
        first_row = df.iloc[0]
        print(f"  DNA Length: {len(first_row['predicted_dna'])} bp")
        print(f"  Protein Length: {len(first_row['protein_sequence'])} aa")
        print(f"  Expected Cases: {first_row['expected_case']}")
    else:
        print("❌ Generation failed")


def example_5_inject_motif():
    """Example 5: Inject ATTATA motif into sequences"""
    print_header("EXAMPLE 5: MOTIF INJECTION (ATTATA)")
    
    # First generate test data if it doesn't exist
    input_path = "generated_test_sequences.csv"
    output_path = "sequences_with_injected_motif.csv"
    
    if not os.path.exists(input_path):
        print_subheader("Preparing Test Data")
        print("Generating test sequences first...")
        generate_test_file.generate_test_file(30, input_path)
    
    print_subheader("Injecting ATTATA Motif")
    print(f"Input file: {input_path}")
    print(f"Output file: {output_path}")
    print("\nInjection strategies:")
    print("  • Case 1: ATT + ATA (Isoleucine codons)")
    print("  • Case 2: GCA + TTA + TAC (Ala + Leu + Tyr)")
    print("  • Case 3: AAT + TAT + ATG (Asn + Tyr + Met)")
    print("\nProcessing...")
    
    results = inject_motif.process_csv(input_path, output_path)
    
    print_subheader("Results")
    if os.path.exists(output_path):
        df_inject = pd.read_csv(output_path)
        print(f"✓ Successfully processed {len(df_inject)} sequences")
        print(f"✓ Saved to: {output_path}")
        
        if 'all_changes' in results:
            total_changes = len(results['all_changes'])
            print(f"✓ Total genetic changes made: {total_changes}")
        
        print(f"\nFirst modified sequence preview:")
        first = df_inject.iloc[0]
        print(f"  Original DNA length: {len(first['predicted_dna'])} bp")
        print(f"  Protein preserved: {first['protein_sequence'][:20]}..." 
              if len(first['protein_sequence']) > 20 
              else f"  Protein: {first['protein_sequence']}")
    else:
        print("❌ Injection failed")


def workflow_complete_pipeline():
    """Complete analysis pipeline"""
    print_header("COMPLETE WORKFLOW: Test → Inject → Analyze")
    
    test_file = "workflow_test_sequences.csv"
    injected_file = "workflow_injected_sequences.csv"
    
    # Step 1: Generate test sequences
    print_subheader("Step 1: Generate Test Sequences")
    print("Creating 100 synthetic sequences...")
    generate_test_file.generate_test_file(100, test_file)
    df_test = pd.read_csv(test_file)
    print(f"✓ Created {len(df_test)} sequences")
    
    # Step 2: Inject motif
    print_subheader("Step 2: Inject ATTATA Motif")
    print("Injecting ATTATA into sequences...")
    inject_motif.process_csv(test_file, injected_file)
    df_injected = pd.read_csv(injected_file)
    print(f"✓ Modified {len(df_injected)} sequences")
    
    # Step 3: Analyze results
    print_subheader("Step 3: Analyze Motif Distribution")
    print("Searching for ATTATA in modified sequences...")
    results = search_motifs_quantity.search_motif(injected_file)
    
    print_subheader("Complete Analysis Results")
    print(f"Total sequences: {results['total_sequences']}")
    print(f"Sequences with ATTATA: {results['num_sequences_with_motif']}")
    print(f"Total ATTATA occurrences: {results['total_occurrences']}")
    print(f"Probability per nucleotide: {results['prob_nucleotide']}")
    print(f"Probability per sequence: {results['prob_sequence']}")
    
    print_subheader("Workflow Complete")
    print(f"✓ All outputs saved in current directory")


def main():
    """Run all examples"""
    print("\n" + "#" * 70)
    print("# DNA SEQUENCE ANALYSIS - QUERY EXAMPLES")
    print("#" * 70)
    print(f"\nPython Environment: {sys.version.split()[0]} | Directory: {os.getcwd()}")
    
    # Run examples
    try:
        example_1_compare_sequences()
        example_2_search_promoter_motif()
        example_3_search_motif_quantity()
        example_4_generate_test_file()
        example_5_inject_motif()
        workflow_complete_pipeline()
        
        print_header("ALL EXAMPLES COMPLETED SUCCESSFULLY")
        print("\n✓ Check the generated CSV files and reports in your working directory")
        print("✓ For interactive examples, run: jupyter notebook queries_examples.ipynb")
        print("✓ For more details, see: README.md in the queries/ directory\n")
        
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
