from collections import Counter

def arrays_similar(seq1, seq2):
    return Counter(seq1) == Counter(seq2)
