# 7kyu - Satisfying numbers

""" 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

Write smallest(n) that will find the smallest positive number that is 
evenly divisible by all of the numbers from 1 to n (n <= 40).

smallest(5) == 60 # 1 to 5 can all divide evenly into 60
smallest(10) == 2520 """

from functools import reduce

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a,b)

def smallest(n):
    return reduce(lcm ,range(1, n + 1))

# from math import gcd
# from functools import reduce

# def smallest(n):
#     return reduce(lambda x, y: (x * y) // gcd(x, y), range(1, n + 1))


q = smallest(1)  # 1
q
q = smallest(2)  # 2
q
q = smallest(3)  # 6
q
q = smallest(4)  # 12
q
q = smallest(5)  # 60
q
q = smallest(6)  # 60
q
q = smallest(7)  # 420
q
q = smallest(8)  # 840
q
q = smallest(9)  # 2520
q
q = smallest(10)  # 2520
q
