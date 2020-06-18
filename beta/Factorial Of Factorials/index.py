""" Beta - Factorial Of Factorials

Find factorial of a factorial.

n = 4, then,
fof(4) = 4! * 3! * 2! * 1! = 288

Write a funtion fof(n), which takes n as input and returns the factorial of factorial. """

from functools import reduce
from math import factorial
from operator import mul

# def factorial(n):
#     return n * factorial(n-1) if n > 0 else 1


def fof(n):
    return reduce(mul, map(factorial, range(1, n+1)))


q = fof(4), 288
q
q = fof(1), 1
q
q = fof(5), 34560
q
