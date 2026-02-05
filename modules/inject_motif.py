import pandas as pd
from itertools import product
from Bio.Seq import Seq
from Bio.Data import CodonTable
from tqdm import tqdm
import os

# Load standard codon table
codon_table = CodonTable.unambiguous_dna_by_id[1]

# Prepare synonymous codons dictionary
synonymous_codons = {}
for codon, aa in codon_table.forward_table.items():
    synonymous_codons.setdefault(aa, []).append(codon)

def insert_attata_motif(dna_seq, protein_seq):
    """
    Perform all possible non-overlapping ATTATA insertions, while preserving the protein sequence.
    """
    seq_length = len(dna_seq)
    modified_seq = list(dna_seq)
    i = 0  # Scan index
    motif = "ATTATA"
    total_insertions = 0
    all_changes = []
    insertion_cases = []

    while i <= seq_length - 6:
        offset = i % 3
        inserted = False  # Flag to track if insertion happened

        # Case 1: 'ATT' 'ATA'
        if offset == 0:
            codon1 = dna_seq[i:i + 3]
            codon2 = dna_seq[i + 3:i + 6]
            if len(codon1) == 3 and len(codon2) == 3:
                if str(Seq(codon1).translate()) == 'I' and str(Seq(codon2).translate()) == 'I':
                    for c1_new, c2_new in product(synonymous_codons['I'], repeat=2):
                        if c1_new + c2_new == motif:
                            changes = []
                            for j in range(3):
                                if modified_seq[i + j] != c1_new[j]:
                                    changes.append((f"Insertion_{total_insertions + 1}", i + j, modified_seq[i + j], c1_new[j]))
                                    modified_seq[i + j] = c1_new[j]
                            for j in range(3):
                                if modified_seq[i + 3 + j] != c2_new[j]:
                                    changes.append((f"Insertion_{total_insertions + 1}", i + 3 + j, modified_seq[i + 3 + j], c2_new[j]))
                                    modified_seq[i + 3 + j] = c2_new[j]
                            all_changes.extend(changes)
                            insertion_cases.append(1)
                            total_insertions += 1
                            i += 6
                            inserted = True
                            break
        # Case 2: "?A-TTA-TA?"
        if not inserted and offset == 2:
            codon1_start = i - 2
            codon2_start = i + 1
            codon3_start = i + 4
            if 0 <= codon1_start < seq_length - 2 and 0 <= codon3_start < seq_length - 2:
                codon1, codon2, codon3 = dna_seq[codon1_start:codon1_start + 3], dna_seq[codon2_start:codon2_start + 3], dna_seq[codon3_start:codon3_start + 3]
                aa1, aa2, aa3 = map(lambda c: str(Seq(c).translate()), [codon1, codon2, codon3])
                if '*' not in (aa1, aa2, aa3):
                    c1_opts = [c for c in synonymous_codons.get(aa1, []) if c.endswith('A')]
                    c2_opts = [c for c in synonymous_codons.get(aa2, []) if c == 'TTA']
                    c3_opts = [c for c in synonymous_codons.get(aa3, []) if c.startswith('TA')]
                    for c1_new, c2_new, c3_new in product(c1_opts, c2_opts, c3_opts):
                        if c1_new[-1] + c2_new + c3_new[:2] == motif:
                            changes = []
                            for j in range(3):
                                if modified_seq[codon1_start + j] != c1_new[j]:
                                    changes.append((f"Insertion_{total_insertions + 1}", codon1_start + j, modified_seq[codon1_start + j], c1_new[j]))
                                    modified_seq[codon1_start + j] = c1_new[j]
                            for j in range(3):
                                if modified_seq[codon2_start + j] != c2_new[j]:
                                    changes.append((f"Insertion_{total_insertions + 1}", codon2_start + j, modified_seq[codon2_start + j], c2_new[j]))
                                    modified_seq[codon2_start + j] = c2_new[j]
                            for j in range(3):
                                if modified_seq[codon3_start + j] != c3_new[j]:
                                    changes.append((f"Insertion_{total_insertions + 1}", codon3_start + j, modified_seq[codon3_start + j], c3_new[j]))
                                    modified_seq[codon3_start + j] = c3_new[j]
                            all_changes.extend(changes)
                            insertion_cases.append(2)
                            total_insertions += 1
                            i += 6
                            inserted = True
                            break

        # Case 3: "?AT-TAT-A?"
        if not inserted and offset == 1:
            codon1_start = i - 1
            codon2_start = i + 2
            codon3_start = i + 5
            if 0 <= codon1_start < seq_length - 2 and 0 <= codon3_start < seq_length - 2:
                codon1, codon2, codon3 = dna_seq[codon1_start:codon1_start + 3], dna_seq[codon2_start:codon2_start + 3], dna_seq[codon3_start:codon3_start + 3]
                aa1, aa2, aa3 = map(lambda c: str(Seq(c).translate()), [codon1, codon2, codon3])
                if '*' not in (aa1, aa2, aa3):
                    c1_opts = [c for c in synonymous_codons.get(aa1, []) if c.endswith('AT')]
                    c2_opts = [c for c in synonymous_codons.get(aa2, []) if c == 'TAT']
                    c3_opts = [c for c in synonymous_codons.get(aa3, []) if c.startswith('A')]
                    for c1_new, c2_new, c3_new in product(c1_opts, c2_opts, c3_opts):
                        if c1_new[-2:] + c2_new + c3_new[0] == motif:
                            changes = []
                            for j in range(3):
                                if modified_seq[codon1_start + j] != c1_new[j]:
                                    changes.append((f"Insertion_{total_insertions + 1}", codon1_start + j, modified_seq[codon1_start + j], c1_new[j]))
                                    modified_seq[codon1_start + j] = c1_new[j]
                            for j in range(3):
                                if modified_seq[codon2_start + j] != c2_new[j]:
                                    changes.append((f"Insertion_{total_insertions + 1}", codon2_start + j, modified_seq[codon2_start + j], c2_new[j]))
                                    modified_seq[codon2_start + j] = c2_new[j]
                            for j in range(3):
                                if modified_seq[codon3_start + j] != c3_new[j]:
                                    changes.append((f"Insertion_{total_insertions + 1}", codon3_start + j, modified_seq[codon3_start + j], c3_new[j]))
                                    modified_seq[codon3_start + j] = c3_new[j]
                            all_changes.extend(changes)
                            insertion_cases.append(3)
                            total_insertions += 1
                            i += 6
                            inserted = True
                            break
        if not inserted:
            i += 1  # No insertion, just advance

    return ''.join(modified_seq), total_insertions, all_changes, insertion_cases

def process_csv(input_path, output_filename):
    df = pd.read_csv(input_path, dtype={0: str, 2: str})
    results = []
    existing_motif_count = 0
    inserted_count = 0
    total_sequences = len(df)

    for _, row in tqdm(df.iterrows(), total=total_sequences, desc="Processing Sequences"):
        dna_seq = row["predicted_dna"].upper()
        protein_seq = row["protein_sequence"].upper()
        if "ATTATA" in dna_seq:
            existing_motif_count += 1
            result = {
                "Original DNA": dna_seq,
                "Modified DNA": dna_seq,
                "Num Insertions": 0,
                "Changes": [],
                "Existing Motif": True,
                "Cases": []
            }
        else:
            mod_seq, num_ins, changes, cases = insert_attata_motif(dna_seq, protein_seq)
            if num_ins > 0:
                inserted_count += 1
            result = {
                "Original DNA": dna_seq,
                "Modified DNA": mod_seq,
                "Num Insertions": num_ins,
                "Changes": changes,
                "Existing Motif": False,
                "Cases": cases
            }
        results.append(result)

    df = pd.DataFrame(results)
    df.to_csv(output_filename, index=False)
    formatted_total_sequences = f"{total_sequences:,}"
    formatted_sequences_with_existing_motif = f"{existing_motif_count:,}"
    formatted_prob_sequences_with_existing_motif = f"{existing_motif_count / total_sequences * 100:.2f}"
    formatted_sequences_without_motif = f"{total_sequences - existing_motif_count:,}"
    formatted_prob_sequences_without_motif = f"{(total_sequences - existing_motif_count) / total_sequences * 100:.2f}"
    formatted_sequences_insertion_possible = f"{inserted_count:,}"
    formatted_prob_sequences_insertion_possible = f"{inserted_count / (total_sequences - existing_motif_count) * 100:.2f}"

    return {
        "total_sequences": formatted_total_sequences,
        "sequences_with_existing_motif": formatted_sequences_with_existing_motif,
        "prob_sequences_with_existing_motif": formatted_prob_sequences_with_existing_motif,
        "sequences_without_motif": formatted_sequences_without_motif,
        "prob_sequences_without_motif": formatted_prob_sequences_without_motif,
        "sequences_insertion_possible": formatted_sequences_insertion_possible,
        "prob_sequences_insertion_possible": formatted_prob_sequences_insertion_possible
    }