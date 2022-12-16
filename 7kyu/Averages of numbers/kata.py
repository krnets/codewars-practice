from itertools import pairwise

def averages(arr):
    return [(x + y) / 2 for x, y in pairwise(arr)] if arr else []


q = averages([2, 2, 2, 2, 2])
q
#     [2, 2, 2, 2]
q = averages([2, -2, 2, -2, 2])
q
#     [0, 0, 0, 0]
q = averages([1, 3, 5, 1, -10])
q
#     [2, 4, 3, -4.5]
q = averages([])
q
#     []
