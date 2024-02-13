# def hamming(a, b):
#     return sum(c != d for c, d in zip(a, b))

from operator import ne


def hamming(a, b):
    return sum(map(ne, a, b))
