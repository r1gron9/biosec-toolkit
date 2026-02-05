import pandas as pd
from collections import defaultdict
import os


def search_motif(csv_path, motif="ATTATA"):
    df = pd.read_csv(csv_path)
    df = df.rename(columns={"Unnamed: 0": "Serial"})
    df = df[df["Serial"].notna()][["Serial", "Id", "predicted_dna", "protein_sequence", "organism_name"]]

    duplicate_sequence_groups = defaultdict(list)
    for _, row in df.iterrows():
        duplicate_sequence_groups[row["protein_sequence"].strip()].append(row["Serial"])
    duplicate_sequence_groups = {k: v for k, v in duplicate_sequence_groups.items() if len(v) > 1}

    duplicates_data = []
    for seq, serials in duplicate_sequence_groups.items():
        duplicates_data.append(["Sequence", seq, ", ".join(map(str, serials))])

    if duplicates_data:
        duplicates_df = pd.DataFrame(duplicates_data, columns=["Type", "Value", "Serial Numbers"])
        duplicates_df.to_csv("duplicates_report.csv", index=False)

    df = df.drop_duplicates(subset=["protein_sequence"], keep="first")
    df.to_csv("cleaned_database.csv", index=False)

    id_duplicates = df["Id"].duplicated().sum()
    sequence_duplicates = df["protein_sequence"].duplicated().sum()

    uniqueness_message = "A test was successfully performed that all proteins from the original database are different from each other."
    if id_duplicates > 0 or sequence_duplicates > 0:
        uniqueness_message = f"Duplicate Ids: {id_duplicates}, Duplicate Sequences: {sequence_duplicates}"

    results = []
    total_occurrences = 0
    total_nucleotides = 0
    total_sequences = len(df)

    for _, row in df.iterrows():
        serial, seq_id, dna_seq = row["Serial"], row["Id"], row["predicted_dna"]
        count = dna_seq.count(motif)
        total_occurrences += count
        total_nucleotides += len(dna_seq)
        if count > 0:
            results.append((serial, seq_id, count))

    results_df = pd.DataFrame(results, columns=["Serial", "Id", "Occurrences"])
    results_df = results_df.sort_values(by=["Serial", "Id"])

    num_sequences_with_motif = len(results_df)
    prob_nucleotide = total_occurrences / total_nucleotides if total_nucleotides > 0 else 0
    prob_sequence = num_sequences_with_motif / total_sequences if total_sequences > 0 else 0

    formatted_total_nucleotides = f"{total_nucleotides:,}"
    formatted_total_occurrences = f"{total_occurrences:,}"
    formatted_total_sequences = f"{total_sequences:,}"
    formatted_sequences_with_motif = f"{num_sequences_with_motif:,}"

    return {
        "results_df": results_df.to_html(classes="table table-striped", index=False),
        "uniqueness_message": uniqueness_message,
        "num_sequences_with_motif": formatted_sequences_with_motif,
        "total_occurrences": formatted_total_occurrences,
        "total_nucleotides": formatted_total_nucleotides,
        "total_sequences": formatted_total_sequences,
        "prob_nucleotide": f"{prob_nucleotide:.2e}",
        "prob_sequence": f"{prob_sequence:.2e}",
    }
