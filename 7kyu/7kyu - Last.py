# 7kyu - Last

""" Find the last element of the given argument(s).

last([1, 2, 3, 4]) ==>  4
last("xyz")        ==> "z"
last(1, 2, 3, 4)   ==>  4

In javascript and CoffeeScript a list will be an array, a string or the list of arguments. """


# def last(*args):
#     end = args[-1]
#     return end[-1] if isinstance(end, (str, list, tuple)) else end

# def last(*args):
#     try:
#         return args[-1][-1]
#     except TypeError:
#         return args[-1]

# def last(*args):
#     return args[-1] if not hasattr(args[-1], '__getitem__') else args[-1][-1]

from collections import Iterable

def last(*args):
    return args[-1][-1] if isinstance(args[-1], Iterable) else args[-1]


q = last([1, 2, 3, 4, 5]), 5
q
q = last("abcde"), "e"
q
q = last(1, "b", 3, "d", 5), 5
q
