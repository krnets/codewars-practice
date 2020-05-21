# 6kyu - Odd/Even number of divisors

""" Given an integer n return 'odd' if the number of its divisors is odd. Otherwise return 'even'.

All prime numbers have exactly two divisors (hence 'even')

For n=12 the divisors are [1,2,3,4,6,12] – 'even'
For n=4 the divisors are [1,2,4] – 'odd' """

# from math import sqrt

# def oddity(n):
#     divisors = [1]
#     for i in range(2, int(sqrt(n) + 1)):
#         if n % i == 0:
#             divisors.append(i)
#     # return 'even' if len(divisors) % 2 == 0 else 'odd'
#     return divisors

# import collections
# import itertools


# def prime_factors(n):
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             n /= i
#             yield i
#         else:
#             i += 1

#     if n > 1:
#         yield n


# def prod(iterable):
#     result = 1
#     for i in iterable:
#         result *= i
#     return result


# def get_divisors(n):
#     pf = prime_factors(n)

#     pf_with_multiplicity = collections.Counter(pf)

#     powers = [[factor ** i for i in range(count + 1)]
#               for factor, count in pf_with_multiplicity.items()]

#     for prime_power_combo in itertools.product(*powers):
#         yield prod(prime_power_combo)


# def oddity(n):
#     return 'odd' if len(list(get_divisors(n))) % 2 else 'even'

# def oddity(n):
#     return 'odd' if n**0.5 == int(n**0.5) else 'even'

# def oddity(n):
#     return ['even', 'odd'][n**0.5 == int(n**0.5)]

# def oddity(n):
#     return ['even', 'odd'][n ** 0.5 == int(n ** 0.5)]

import math

def oddity(n):
    return ['even', 'odd'][math.sqrt(n) % 1 == 0]



q = oddity(1)  # 'odd'
q
q = oddity(5)  # 'even'
q
q = oddity(16)  # 'odd'
q
