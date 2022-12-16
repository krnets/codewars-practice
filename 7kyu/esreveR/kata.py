# 7kyu - esreveR

"""
Remove this comment otherwise your code cannot pass the anti-cheat tests!

You are not allowed to use the following:
    - python 2
    - slice notations
    - defining an empty list: []. Use " x = list() " instead
    - list comprehensions
    - the spread operator inside square brackets
    - "tuple" and "reversed" builtins have been deactivated

The "list" builtin has been replaced with another implementation with the following specifications:
    - list.reverse is forbidden
    - list.__reversed__ is forbidden
    - slicing is forbidden
All other usual methods of the list class are still present.
"""

# def reverse(lst):
#     result = list()  # use this!
#     n = len(lst)

#     for i in range(n):
#         result.append(lst.pop())

#     return result


def reverse(lst):
    result = list()
    while lst:
        result.append(lst.pop())
    return result


q = reverse(list([1, 2, 3]))  # [3,2,1]
q
q = reverse(list([1, None, 14, "two"]))  # ["two",14,None,1]
q
