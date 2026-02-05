import pandas as pd
import random
from Bio.Seq import Seq
from Bio.Data import CodonTable

# Load standard codon table
codon_table = CodonTable.unambiguous_dna_by_id[1]

# Prepare synonymous codon dictionary
synonymous_codons = {}
for codon, aa in codon_table.forward_table.items():
    synonymous_codons.setdefault(aa, []).append(codon)

def random_codon_for_aa(aa, exclude=None):
    options = [c for c in synonymous_codons[aa] if c != exclude]
    return random.choice(options) if options else exclude

def generate_case_sequence(case_num):
    codon_length = 3
    if case_num == 1:
        c1 = random_codon_for_aa('I', exclude='ATT')
        c2 = random_codon_for_aa('I', exclude='ATA')
        sequence = c1 + c2
    elif case_num == 2:
        c1 = random_codon_for_aa('A', exclude='GCA')
        c2 = 'TTA'
        c3 = random_codon_for_aa('Y', exclude='TAC')
        sequence = c1 + c2 + c3
    elif case_num == 3:
        c1 = random_codon_for_aa('N', exclude='AAT')
        c2 = 'TAT'
        c3 = random_codon_for_aa('M', exclude='ATG')
        sequence = c1 + c2 + c3
    return sequence, len(sequence) // codon_length

def generate_test_file(total_sequences, output_path):
    test_entries = []
    for _ in range(total_sequences):
        expected_case_list = []
        num_cases = random.randint(1, 3)
        dna_seq = ""
        codon_pos = 1
        for _ in range(num_cases):
            case_num = random.choice([1, 2, 3])
            case_dna, codon_offset = generate_case_sequence(case_num)
            dna_seq += case_dna
            expected_case_list.append(f"(case {case_num}: start in codon {codon_pos})")
            codon_pos += codon_offset
        for _ in range(random.randint(0, 2)):
            dna_seq += random_codon_for_aa('S')
        if len(dna_seq) % 3 != 0:
            dna_seq += 'A' * (3 - len(dna_seq) % 3)
        protein_seq = str(Seq(dna_seq).translate())
        test_entries.append({
            "predicted_dna": dna_seq,
            "protein_sequence": protein_seq,
            "expected_case": "[" + ", ".join(expected_case_list) + "]"
        })
    df = pd.DataFrame(test_entries)
    df.to_csv(output_path, index=False)
    return output_path
