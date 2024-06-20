from math import pi


def sort_by_area(seq):
    return sorted(seq, key=calc_area)


def calc_area(dim):
    return dim[0] * dim[1] if isinstance(dim, tuple) else pi * dim**2
