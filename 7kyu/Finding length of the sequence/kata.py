def length_of_sequence(arr, n):
    indices = [i for i, x in enumerate(arr) if x == n]
    return indices[-1] - indices[0] + 1 if len(indices) == 2 else 0
