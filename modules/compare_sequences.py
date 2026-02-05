from Bio.Seq import Seq

def compare_seq(seq1, seq2):
    """Simple sequence comparison - count differences"""
    seq1 = str(seq1).upper()
    seq2 = str(seq2).upper()
    min_len = min(len(seq1), len(seq2))
    differences = sum(1 for i in range(min_len) if seq1[i] != seq2[i])
    differences += abs(len(seq1) - len(seq2))
    return {
        "differences": differences,
        "seq1_length": len(seq1),
        "seq2_length": len(seq2)
    }


def display_results(sequence1, sequence2, optimizer1, optimizer2):
    seq1 = Seq(sequence1.upper().replace(" ", ""))
    seq2 = Seq(sequence2.upper().replace(" ", ""))
    reverse1 = seq1.reverse_complement()
    reverse2 = seq2.reverse_complement()

    colored_seq1, colored_seq2 = color_triplet_comparison(seq1, seq2)
    counts = count_triplet_differences(seq1, seq2)

    motifs = ["TATAAT"]
    highlighted_reverse1, found_motifs1 = find_motifs(str(reverse1), motifs)
    highlighted_reverse2, found_motifs2 = find_motifs(str(reverse2), motifs)

    result = f"""
    <div class='section'>
        <h2 class='section-title'>Original Sequence Comparison (Triplets Highlighted)</h2>
        <p><strong>{optimizer1}:</strong></p>
        <code>{colored_seq1}</code>
        <br><br>
        <p><strong>{optimizer2}:</strong></p>
        <code>{colored_seq2}</code>
        <br><br>
        <p><strong>Differences per triplet index:</strong> 
        <span style="color:red">Index 1</span>: {counts[0]}, 
        <span style="color:orange">Index 2</span>: {counts[1]}, 
        <span style="color:blue">Index 3</span>: {counts[2]}</p>
    </div>
    <div class='section'>
        <h2 class='section-title'>Reverse Complement Analysis</h2>
        <p><strong>Reverse Complement of {optimizer1}:</strong></p>
        <code>{highlighted_reverse1}</code>
        <br><br>
        <p><strong>Reverse Complement of {optimizer2}:</strong></p>
        <code>{highlighted_reverse2}</code>
    </div>
    <div class='section'>
        <h2 class='section-title'>Motif Search</h2>
        <p><strong>Motifs Searched:</strong> {', '.join(motifs)}</p>
        <p><strong>Motifs Found in {optimizer1}:</strong> {', '.join(found_motifs1) if found_motifs1 else 'No motifs found'}</p>
        <p><strong>Motifs Found in {optimizer2}:</strong> {', '.join(found_motifs2) if found_motifs2 else 'No motifs found'}</p>
    </div>
    """
    return result


def color_triplet_comparison(seq1, seq2):
    colored_seq1 = ""
    colored_seq2 = ""
    triplet_length = 3

    for i in range(0, min(len(seq1), len(seq2)), triplet_length):
        triplet1 = seq1[i:i + triplet_length]
        triplet2 = seq2[i:i + triplet_length]

        for j in range(triplet_length):
            color = ""
            if i + j >= len(seq1) or i + j >= len(seq2):
                continue
            if triplet1[j] != triplet2[j]:
                if j == 0:
                    color = "red"
                elif j == 1:
                    color = "orange"
                elif j == 2:
                    color = "blue"
                colored_seq1 += f'<span style="color:{color};">{triplet1[j]}</span>'
                colored_seq2 += f'<span style="color:{color};">{triplet2[j]}</span>'
            else:
                colored_seq1 += triplet1[j]
                colored_seq2 += triplet2[j]

        colored_seq1 += " "
        colored_seq2 += " "

    return colored_seq1.strip(), colored_seq2.strip()


def count_triplet_differences(seq1, seq2):
    counts = [0, 0, 0]
    for i in range(0, min(len(seq1), len(seq2)), 3):
        for j in range(3):
            if i + j >= len(seq1) or i + j >= len(seq2):
                continue
            if seq1[i + j] != seq2[i + j]:
                counts[j] += 1
    return counts


def find_motifs(sequence, motifs):
    highlighted = sequence
    found = []

    for motif in motifs:
        if motif in highlighted:
            found.append(motif)
        highlighted = highlighted.replace(motif, f"<mark>{motif}</mark>")
    return highlighted, found
