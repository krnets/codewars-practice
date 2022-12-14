""" Given a two-dimensional array of integers, 
return the flattened version of the array 
with all the integers in the sorted (ascending) order """

from itertools import chain

# def flatten_and_sort(array):
#     return sorted([*chain(*array)])


def flatten_and_sort(array):
    return sorted((chain(*array)))


q = flatten_and_sort([])  # []
q
q = flatten_and_sort([[], []])  # []
q
q = flatten_and_sort([[], [1]])  # [1]
q
q = flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
q
q = flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]])  # [1, 2, 3, 4, 5, 6, 100])
q
