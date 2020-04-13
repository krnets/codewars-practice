# 7kyu - esreveR

""" Write a function reverse which reverses a list.
(the dedicated builtin(s) functionalities are deactivated)

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
All other usual methods of the list class are still present."""

# def reverse(lst):
#     res = list()
#     while len(lst):
#         res.append(lst.pop())
#     return res

def reverse(lst):
    res = list()
    while lst:
        res.append(lst.pop())
    return res

# def reverse(lst):
#     res = list()
#     for i in range(len(lst)):
#         res.append(lst.pop())
#     return res


q = reverse(list([1, 2, 3]))  # [3,2,1]
q
q = reverse(list([1, None, 14, "two"]))  # ["two",14,None,1]
q
