from itertools import pairwise


def all_non_consecutive(arr):
    return [{"i": i, "n": y} for i, (x, y) in enumerate(pairwise(arr), 1) if y - x != 1]
