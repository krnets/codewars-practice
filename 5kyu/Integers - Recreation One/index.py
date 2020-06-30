""" 5kyu - Integers: Recreation One

Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. 
These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764. 
The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n 
whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of tuples or a string, each subarray having two elements, 
first the number whose squared divisors is a square and then the sum of the squared divisors. """

# CACHE = {}

# def divs_squared(n):
#     if n not in CACHE:
#         divisors = [i for i in range(1, n+1) if n % i == 0]
#         CACHE[n] = sum((x * x for x in divisors))
#         return CACHE[n]
#     return CACHE[n]

# def divs_squared(n):
#     if n not in CACHE:
#         CACHE[n] = sum(x * x for x in [i for i in range(1, n+1) if n % i == 0])
#         return CACHE[n]
#     return CACHE[n]

# def list_squared(m, n):
#     res = []
#     for i in range(m, n+1):
#         ds = divs_squared(i)
#         if (ds ** 0.5) % 1 == 0:
#             res.append([i, ds])
#     return res

# def list_squared(m, n):
#     return [[i, ds] for i in range(m, n+1) if ((ds := divs_squared(i))**.5).is_integer()]

from functools import reduce
from itertools import chain


def factors(n):
    return set(chain.from_iterable([d, n // d] for d in range(1, int(n**0.5) + 1) if n % d == 0))


def divs_squared_sum(n):
    return reduce(lambda s, d: s + d**2, factors(n))


def list_squared(m, n):
    res = []
    for x in range(m, n+1):
        ds = divs_squared_sum(x)
        if (ds ** 0.5) % 1 == 0:
            res.append([x, ds])
    return res


q = list_squared(1, 5), [[1, 1]]
q
q = list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]]
q
q = list_squared(42, 250), [[42, 2500], [246, 84100]]
q
q = list_squared(250, 500), [[287, 84100]]
q
