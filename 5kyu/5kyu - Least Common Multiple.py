# 5kyu - Least Common Multiple

""" Compute the least common multiple of some non-negative integers
Write a function that calculates the least common multiple of its arguments; each argument is assumed to be a non-negative integer. 
In the case that there are no arguments (or the provided array in compiled languages is empty), return 1. """

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     return a * b / gcd(a, b)

# def lcm(*args):
#     if len(args) == 1:
#         return args[0]
#     arr = []
#     for i in range(len(args) - 1):
#         res = (args[i] * args[i+1]) / gcd(args[i], args[i+1])
#         arr.append(res)
#     return int(max(arr))

from functools import reduce
from fractions import gcd

def lcm(*args):
    return reduce(lambda a, b: a * b / gcd(a, b), args)

q = lcm(2, 5)  # 10
q
q = lcm(2, 3, 4)  # 12
q
q = lcm(9)  # 9
q
q = lcm(0)  # 0
q
q = lcm(0, 1)  # 0
q
