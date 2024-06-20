# def next_higher(n):
#     n_bits = n.bit_count()
#     m = n + 1
#     while m.bit_count() != n_bits:
#         m += 1
#     return m

from itertools import count

def next_higher(n):
    n_bits = n.bit_count()
    return next(i for i in count(n + 1) if i.bit_count() == n_bits)
