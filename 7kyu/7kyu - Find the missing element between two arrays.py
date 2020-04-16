# 7kyu - Find the missing element between two arrays

""" Given two integer arrays where the second array is a shuffled duplicate of the 
first array with one element missing, find the missing element.

Please note, there may be duplicates in the arrays, so checking if a numerical value 
exists in one and not the other is not a valid solution.

find_missing([1, 2, 2, 3], [1, 2, 3]) => 2
find_missing([6, 1, 3, 6, 8, 2], [3, 6, 6, 1, 2]) => 8

The first array will always have at least one element."""

# from collections import Counter

# def find_missing(arr1, arr2):
#     return [x for x in (Counter(arr1) - Counter(arr2)).keys()][0]

from functools import reduce
from itertools import chain
from operator import xor

def find_missing(arr1, arr2):
    return reduce(xor, chain(arr1, arr2))

# def find_missing(arr1, arr2):
#     return sum(arr1) - sum(arr2)


# def find_missing(arr1, arr2):
#     return [x for x in set(arr1 + arr2) if arr1.count(x) != arr2.count(x)].pop()

# def find_missing(arr1, arr2):
#     return next(x for x in set(arr1 + arr2) if arr1.count(x) != arr2.count(x))


q = find_missing([1, 2, 3], [1, 3])  # 2
q
q = find_missing([6, 1, 3, 6, 8, 2], [3, 6, 6, 1, 2])  # 8
q
q = find_missing([7], [])  # 7
q
q = find_missing([4, 3, 3, 61, 8, 8], [8, 61, 8, 3, 4])  # 3
q
q = find_missing([0, 0, 0, 0, 0], [0, 0, 0, 0])  # 0
q
