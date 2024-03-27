def binary_cleaner(seq):
    return [*filter(lambda x: x <= 1, seq)], [i for i, x in enumerate(seq) if x > 1]
