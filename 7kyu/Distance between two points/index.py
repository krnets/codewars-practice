# 7kyu - Distance between two points

""" Program the function distance(p1, p2) which returns the distance between the points p1 and p2 
in n-dimensional space. p1 and p2 will be given as arrays.

Your program should work for all lengths of arrays, and should return -1 if the arrays aren't of the same length 
or if both arrays are empty sets.

If you don't know how to measure the distance between two points, go here: http://mathworld.wolfram.com/Distance.html """


# def distance(p1, p2):
#     res = sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5
#     return -1 if res == 0 or len(p1) != len(p2) else res

# def distance(p1, p2):
#     return sum((a - b) ** 2 for a, b in zip(p1, p2)) ** 0.5 if len(p1) == len(p2) > 0 else -1

from functools import reduce
from math import hypot

def distance(p1, p2):
    if not p1 or len(p1) != len(p2):
        return -1
    return reduce(hypot, (x-y for x, y in zip(p1, p2)))


# test.describe("Normal cases")
q = distance([2, 2], [1, 1])  # 2**0.5
q
q = distance([4], [1])  # 3
q
q = distance([1, 1, 1], [0, 0, 0])  # 3**0.5
q
q = distance([2, 1, 3, 1], [2, 0, 2, -1])  # 6**0.5
q
q = distance([3, 2, 3], [0, 1, 1])  # 14**0.5
q

# test.describe("Bad input/edge cases")
q = distance([], [])  # -1
q
q = distance([1], [1, 1, 1, 1, 1, 1, 1, 1, 1])  # -1
q
