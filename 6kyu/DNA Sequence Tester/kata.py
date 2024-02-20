def check_DNA(seq1, seq2):
    if len(seq1) > len(seq2):
        seq1, seq2 = seq2, seq1
    return seq1.translate(str.maketrans("ATCG", "TAGC")) in seq2[::-1]
