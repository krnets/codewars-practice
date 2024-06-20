# def generate_pairs(n):
#     res = []
#     for i in range(n + 1):
#         for j in range(i, n + 1):
#             res.append([i, j])
#     return res


# def generate_pairs(n):
#     return [[i, j] for i in range(n + 1) for j in range(i, n + 1)]

from itertools import combinations_with_replacement


def generate_pairs(n):
    return [*map(list, combinations_with_replacement(range(n + 1), 2))]
