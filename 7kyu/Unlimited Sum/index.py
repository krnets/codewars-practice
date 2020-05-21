# 7kyu - Unlimited Sum

""" Write a function sum that accepts an unlimited number of integer arguments, and adds all of them together.

The function should reject any arguments that are not integers, and sum the remaining integers.

sum(1, 2, 3)    ==>  6
sum(1, "2", 3)  ==>  4 """

# from functools import reduce

# def sum(*args):
#     return reduce(lambda x, y: x + y, [x for x in args if isinstance(x, int)])

from functools import reduce
from operator import add

def sum(*args):
    return reduce(add, [x for x in args if isinstance(x, int)])


q = sum(1, 2, 3)  # 6
q
q = sum(1, "2", 3)  # 4
q
