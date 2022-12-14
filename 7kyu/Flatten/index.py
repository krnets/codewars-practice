# 7kyu - Flatten

""" Write a function that flattens an Array of Array objects into a flat Array. 
Your function must only do one level of flattening."""


from itertools import chain
from typing import Iterable


# def flatten(lst):
#     try:
#         return list(chain.from_iterable(lst))
#     except:
#         return lst

# def flatten(lst):
#     try:
#         return list(chain(*lst))
#     except:
#         return lst

# def flatten(lst):
#     return [x for y in lst for x in y] if any(x for x in lst if isinstance(x, list)) else lst


# def flatten(lst):
#     return [x for y in lst for x in (y if isinstance(y, list) else [y])]


# def flatten(lst):
#     result = []
#     for x in lst:
#         if isinstance(x, list):
#             result.extend(x)
#         else:
#             result.append(x)
#     return result


# def flatten(lst):
#     try:
#         return sum(map(list, lst), [])
#     except:
#         return lst


def flatten(lst):
    return [*chain.from_iterable(lst)] if lst and isinstance(lst[0], Iterable) else lst


q = flatten([])  # []
q
q = flatten([1, 2, 3])  # [1,2,3]
q
q = flatten([[1, 2, 3], ["a", "b", "c"], [1, 2, 3]])
q
#     [1,2,3,"a","b","c",1,2,3]
q = flatten([[1, 2, 3], ["a", "b", "c"], [1, 2, 3], "a"])
q
#     [1,2,3,"a","b","c",1,2,3,"a"]
q = flatten([[3, 4, 5], [[9, 9, 9]], ["a,b,c"]])
q
#     [3,4,5,[9,9,9],"a,b,c"]
q = flatten([[[3], [4], [5]], [9], [9], [8], [[1, 2, 3]]])
q
#     [[3], [4], [5], 9, 9, 8, [1, 2, 3]]
