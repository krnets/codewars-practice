from itertools import groupby


def longest_sequence(arr, elem):
    return max(len(list(g)) for x, g in groupby(arr) if x == elem)
