# 7kyu - Big Factorial

""" The factorial of a number, n!, is defined for whole numbers as the product of all integers from 1 to n.

For example, 5! is 5 * 4 * 3 * 2 * 1 = 120

Most factorial implementations use a recursive function to determine the value of factorial(n). 
However, this blows up the stack for large values of n - most systems cannot handle stack depths much greater than 2000 levels.

Write an implementation to calculate the factorial of arbitrarily large numbers, without recursion.

    n < 0 should return None
    n = 0 should return 1
    n > 0 should return n!

Codewars limits the amount of data it will send back and forth, which may introduce a false ceiling 
for how high of a value of n it will accept. All tests use values less than this limit. """

# from operator import mul
# from functools import reduce

# def factorial(n):
#     if n < 0:
#         return None
#     return reduce(mul, range(1, n+1), 1)

import math

def factorial(n):
    return math.factorial(n) if n >= 0 else None


q = factorial(1)  # 1
q
q = factorial(4)  # 24
q
q = factorial(5)  # 120
q
