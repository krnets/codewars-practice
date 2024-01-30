from itertools import groupby


def unique_in_order(sequence):
    return [k for k, _ in groupby(sequence)]
