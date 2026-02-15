import pandas as pd
from collections import defaultdict


def search_motif(csv_path, motif="ATTATA"):
    """
    Analyze motif distribution in CSV file.
    Works with any CSV file containing DNA sequence column.
    """
    df = pd.read_csv(csv_path)
    
    # Find the DNA sequence column (flexible for different formats)
    dna_column = None
    for col in ['Modified DNA', 'predicted_dna', 'Sequence', 'sequence']:
        if col in df.columns:
            dna_column = col
            break
    
    if dna_column is None:
        # Use second column if first column name doesn't match
        dna_column = df.columns[1] if len(df.columns) > 1 else df.columns[0]
    
    # Find the protein sequence column to check uniqueness
    protein_column = None
    for col in ['protein_sequence', 'Protein_sequence', 'protein', 'Protein']:
        if col in df.columns:
            protein_column = col
            break
    
    total_sequences = len(df)
    total_motif_count = 0
    sequences_with_motif = 0
    total_nucleotides = 0
    detailed_results = []
    
    for idx, row in df.iterrows():
        seq = str(row[dna_column]).upper()
        count = seq.count(motif)
        total_motif_count += count
        total_nucleotides += len(seq)
        
        if count > 0:
            sequences_with_motif += 1
        
        # Get sequence ID
        seq_id = row[df.columns[0]] if len(df.columns) > 0 else f"seq_{idx}"
        
        detailed_results.append({
            'Sequence ID': seq_id,
            'Motif Count': count,
            'Sequence Length': len(seq)
        })
    
    # Calculate probabilities
    prob_nucleotide = (total_motif_count / total_nucleotides) if total_nucleotides > 0 else 0
    prob_sequence = (sequences_with_motif / total_sequences) if total_sequences > 0 else 0
    
    # Format probabilities
    prob_nucleotide_str = f"{prob_nucleotide:.2e}"
    prob_sequence_str = f"{prob_sequence:.2e}"
    
    # Check protein uniqueness
    unique_proteins = "N/A"
    if protein_column:
        unique_protein_count = df[protein_column].nunique()
        total_protein_count = len(df)
        uniqueness_message = f"Unique proteins: {unique_protein_count}/{total_protein_count}"
    else:
        uniqueness_message = "Protein sequence column not found"
    
    # Create results dataframe
    results_df = pd.DataFrame(detailed_results)
    results_html = results_df.to_html(index=False, classes='results-table')
    
    return {
        "uniqueness_message": uniqueness_message,
        "total_sequences": total_sequences,
        "num_sequences_with_motif": sequences_with_motif,
        "total_occurrences": total_motif_count,
        "total_nucleotides": total_nucleotides,
        "prob_nucleotide": prob_nucleotide_str,
        "prob_sequence": prob_sequence_str,
        "results_df": results_html
    }
