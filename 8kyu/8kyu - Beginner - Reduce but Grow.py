# 8kyu - Beginner - Reduce but Grow

""" Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24 """


# def grow(arr):
#     from functools import reduce
#     return reduce(lambda acc, x: acc * x, arr)

from functools import reduce
from operator import mul

def grow(arr):
    return reduce(mul, arr)

# def grow(arr):
#     return eval('*'.join([str(i) for i in arr]))

# grow = lambda x: return __import__('functools').reduce(lambda acc, v: acc * v, x)

# def grow(arr):
#     product = 1
#     for x in arr:
#         product *= x
#     return product


q = grow([1, 2, 3])  # 6
q
q = grow([4, 1, 1, 1, 4])  # 16
q
q = grow([2, 2, 2, 2, 2, 2])  # 64
q
