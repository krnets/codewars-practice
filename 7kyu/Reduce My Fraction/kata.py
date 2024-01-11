# def reduce_fraction(fraction):
#     a, b = fraction
#     lcm_res = lcm(a, b)
#     return (lcm_res // b, lcm_res // a)


# def lcm(a, b):
#     return (a * b) / gcd(a, b)


# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a


# def reduce_fraction(fraction):
#     a, b = fraction
#     gcd_res = gcd(a, b)
#     return (a // gcd_res, b // gcd_res)


# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

from fractions import Fraction
from math import gcd


# def reduce_fraction(fraction):
#     num, denom = fraction
#     g = gcd(num, denom)
#     return (num // g, denom // g)


def reduce_fraction(fraction):
    t = Fraction(*fraction)
    return t.numerator, t.denominator
