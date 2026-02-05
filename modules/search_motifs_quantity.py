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
    
    total_sequences = len(df)
    total_motif_count = 0
    sequences_with_motif = 0
    
    for _, row in df.iterrows():
        seq = str(row[dna_column]).upper()
        count = seq.count(motif)
        total_motif_count += count
        if count > 0:
            sequences_with_motif += 1
    
    avg_motifs = total_motif_count / sequences_with_motif if sequences_with_motif > 0 else 0
    
    return {
        "Total Sequences": total_sequences,
        "Sequences with Motif": sequences_with_motif,
        "Total Motif Count": total_motif_count,
        "Average Motifs per Sequence": round(avg_motifs, 2),
    }
