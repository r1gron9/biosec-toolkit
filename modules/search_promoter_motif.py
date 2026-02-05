import pandas as pd

def load_genes(csv_path):
    """Load gene locations from CSV without filtering for strand type."""
    df = pd.read_csv(csv_path)
    df.columns = ["Accession", "Start", "Stop", "Gene_symbol", "Strand", "NCBI_Gene_ID", "Name"]
    df = df.iloc[1:].reset_index(drop=True)  # Remove redundant header row
    df["Start"] = pd.to_numeric(df["Start"], errors='coerce')
    df["Stop"] = pd.to_numeric(df["Stop"], errors='coerce')
    return df

def load_fasta_sequence(fasta_path):
    """Load the nucleotide sequence from a FASTA file."""
    with open(fasta_path, "r") as f:
        lines = f.readlines()
    return "".join(line.strip() for line in lines[1:])  # Ignore the header line

def search_attata(sequence, genes):
    """Search for 'ATTATA' in all gene locations."""
    search_seq = "ATTATA"
    results = []
    total_count = 0
    total_searches = 0  # Counter for sample space

    for _, row in genes.iterrows():
        start, stop = row["Start"], row["Stop"]
        if pd.isna(start) or pd.isna(stop):
            continue  # skip invalid rows
        start = int(start)
        stop = int(stop)

        search_range = sequence[start - 1 : stop]  # Include full gene range
        total_searches += len(search_range)  # Count how many positions are checked

        index = search_range.find(search_seq)
        while index != -1:
            global_index = start + index
            results.append(global_index)
            total_count += 1
            index = search_range.find(search_seq, index + 1)

    return results, total_count, total_searches

def process_files(csv_path, fasta_path):
    genes = load_genes(csv_path)
    sequence = load_fasta_sequence(fasta_path)
    found_indices, count, total_searches = search_attata(sequence, genes)

    probability = (count / total_searches) if total_searches > 0 else 0
    formatted_probability = f"{probability:.2e}"

    result_text = {
        "indices": found_indices,
        "count": count,
        "total_searches": total_searches,
        "probability": formatted_probability
    }
    return result_text
