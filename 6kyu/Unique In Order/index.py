# 6kyu - Unique In Order

""" Implement the function unique_in_order which takes as argument a sequence and returns a list of items 
without any elements with the same value next to each other and preserving the original order of elements. """

# def unique_in_order(iterable):
#     res, prev, curr = [], '', ''
#     for x in iterable:
#         prev = curr
#         curr = x
#         if prev is not curr:
#             res.append(curr)
#     return res

# def unique_in_order(iterable):
#     res = []
#     prev = None
#     for x in iterable:
#         if x != prev:
#             res.append(x)
#             prev = x
#     return res

from itertools import groupby

def unique_in_order(iterable):
    # return [list(g) for k, g in groupby(iterable)]
    return [k for k, g in groupby(iterable)]


q = unique_in_order('AAAABBBCCDAABBB')  # ['A', 'B', 'C', 'D', 'A', 'B']
q
q = unique_in_order('ABBCcAD')  # ['A', 'B', 'C', 'c', 'A', 'D']
q
q = unique_in_order([1, 2, 2, 3, 3])  # [1,2,3]
q
