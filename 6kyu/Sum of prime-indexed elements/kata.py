# from math import sqrt

from gmpy2 import is_prime

def total(arr):
    return sum(x for i, x in enumerate(arr) if is_prime(i))


# def is_prime(n):
#     if n in (2, 3, 5):
#         return True
#     if n < 2 or n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
#         return False
#     for i in range(5, int(sqrt(n)) + 1, 6):
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#     return True
