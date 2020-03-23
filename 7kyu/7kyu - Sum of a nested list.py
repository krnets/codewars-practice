# 7kyu - Sum of a nested list

""" Implement a function to calculate the sum of the numerical values in a nested list.

sum_nested([1, [2, [3, [4]]]]) -> 10 """

# import collections

# from collections import Iterable

# def flatten(x):
#     if isinstance(x, Iterable):
#         return [a for i in x for a in flatten(i)]
#     else:
#         return [x]


# def flatten(lst):
#     for item in lst:
#         try:
#             yield from flatten(item)
#         except TypeError:
#             yield item

# def sum_nested(s):
#     return sum(flatten(s))


def sum_nested(lst):
    return sum(sum_nested(x) if isinstance(x, list) else x for x in lst)


# Should handle non-nested lists
q = sum_nested([1])  # 1
q
q = sum_nested([1, 2, 3, 4])  # 10
q
q = sum_nested(list(range(11)))  # 55
q
# Non-nested edge case
q = sum_nested([])  # 0
q

# Should handle simple nestings
q = sum_nested([[1], []])  # 1
q
q = sum_nested([[1, 2, 3, 4]])  # 10
q

# Simple nesting edge case
q = sum_nested([[], []])  # 0
q

# Should handle more complex nestings
q = sum_nested([1, [1], [[1]], [[[1]]]])  # 4
q
q = sum_nested([1, [1], [1, [1]], [1, [1], [1, [1]]]])  # 8
q

# Complex nesting edge case
q = sum_nested(
    [[[[], [], [[[[[[[[[[]]]]]]]]]]], [], [], [[[], [[]]]]], []])  # 0
q
