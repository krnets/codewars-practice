# 6kyu - Find the odd int

""" Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times. """

# from collections import Counter

# def find_it(seq):
#     return [x for x, y in Counter(seq).items() if y % 2][0]

# from functools import reduce
# from operator import xor

# def find_it(seq):
#     return reduce(xor, seq)

# from functools import reduce

# def find_it(seq):
#     return reduce(lambda x, y: x ^ y, seq)

def find_it(seq):
    return [x for x in set(seq) if seq.count(x) % 2][0]


q = find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])  # 5
q
q = find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])  # -1
q
q = find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])  # 5
q
q = find_it([10])  # 10
q
q = find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1])  # 10
q
q = find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10])  # 1
q
