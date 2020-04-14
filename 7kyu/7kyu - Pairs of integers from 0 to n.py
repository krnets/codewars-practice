# 7kyu - Pairs of integers from 0 to n

""" Write a function generate_pairs that accepts an integer argument n and generates an array 
containing the pairs of integers [a, b] that satisfy the following conditions:

0 <= a <= b <= n

The pairs should be sorted by increasing values of a then increasing values of b.

For example, generate_pairs(2) should return

[ [0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2] ] """

# def generate_pairs(n):
#     arr = list(range(n+1))
#     res = []
#     for i in range(n+1):
#         for j in arr[i:]:
#             res.append([i, j])
#     return res


# def generate_pairs(n):
#     return [[i, j] for i in range(n+1) for j in range(i, n+1)]

from itertools import combinations_with_replacement as cwr

def generate_pairs(n):
    return list(map(list, cwr(range(n+1), 2)))


q = generate_pairs(2)  # [[0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2]]
q
q = generate_pairs(0)  # [[0, 0]]
q
