# 5kyu - By the Power Set of Castle Grayskull

""" Write a function that returns all of the sublists of a list."""

# from itertools import combinations

# def power(a):
#     res = []
#     for i in range(len(a)+1):
#         for c in combinations(a, i):
#             res.append(list(c))
#     return res

# def power(a):
#     return [list(c) for i in range(len(a)+1) for c in combinations(a, i)]

# def power(a):
#     return [c for i in range(len(a)+1) for c in combinations(a, i)]

from itertools import chain, combinations

def power(a):
    return chain.from_iterable(combinations(a, r) for r in range(len(a)+1))

# def power(a):
#     res = [[]]
#     for num in a:
#         res += [x + [num] for x in res]
#     return res


q = power([1, 2, 3])  # =[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
q
