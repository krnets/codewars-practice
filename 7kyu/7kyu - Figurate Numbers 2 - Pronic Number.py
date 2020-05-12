# 7kyu - Figurate Numbers #2 - Pronic Number

""" Create a function isPronic to check whether the argument passed is a Pronic Number 
and return true if it is & false otherwise.

Pronic Number -A pronic number, oblong number, rectangular number or heteromecic number, 
is a number which is the product of two consecutive integers, that is, n(n + 1).

    The first few Pronic Numbers are - 0, 2, 6, 12, 20, 30, 42...

  0 = 0 × 1   // ∴  0 is a Pronic Number
  2 = 1 × 2   // ∴  2 is a Pronic Number
  6 = 2 × 3   // ∴  6 is a Pronic Number
 12 = 3 × 4   // ∴ 12 is a Pronic Number
 20 = 4 × 5   // ∴ 20 is a Pronic Number
 30 = 5 × 6   // ∴ 30 is a Pronic Number
 42 = 6 × 7   // ∴ 42 is a Pronic Number """


# def is_pronic(n):
#     return n in [i * (i+1) for i in range(-1, n)]

# def is_pronic(n):
#     return n in [i * (i+1) for i in range(n+1)]

from math import sqrt

def is_pronic(n):
    if n < 0:
        return False
    s = int(sqrt(n))
    return s * (s + 1) == n


q = is_pronic(0), True
q
q = is_pronic(1), False
q
q = is_pronic(2), True
q
q = is_pronic(3), False
q
q = is_pronic(6), True
q
q = is_pronic(12), True
q
q = is_pronic(20), True
q
q = is_pronic(30), True
q
q = is_pronic(42), True
q
q = is_pronic(52), False
q
