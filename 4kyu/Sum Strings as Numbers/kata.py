# def sum_strings(x, y):
#     if x == "" and y == "": return "0"
#     if x == "": return y
#     if y == "": return x
#     if len(x) > len(y):
#         x, y = y, x
#     i = len(x) - 1
#     j = len(y) - 1
#     carry = False
#     digits = []

#     while i >= 0:
#         z = int(carry) + int(x[i]) + int(y[j])
#         digits.append(z % 10)
#         if z > 9:
#             carry = True
#         else:
#             carry = False
#         i -= 1
#         j -= 1

#     while j >= 0:
#         digits.append(int(carry) + int(y[j]))
#         if digits[-1] > 9:
#             digits[-1] = 0
#             carry = True
#         else:
#             carry = False
#         j -= 1

#     if carry:
#         digits.append(1)
#     if len(digits) > 1 and digits[-1] == 0:
#         digits.pop()
#     return "".join(map(str, reversed(digits)))

from itertools import zip_longest
from gmpy2 import mpz


# def sum_strings(x, y):
#     return str(mpz(x or "0") + mpz(y or "0"))


def sum_strings(x, y):
    if x in ("", "0") and y in ("", "0"):
        return "0"
    digits, carry = [], 0

    for a, b in zip_longest(map(int, reversed(x)), map(int, reversed(y)), fillvalue=0):
        m = a + b + carry
        digits.append(m % 10)
        carry = (0, 1)[m > 9]

    return "".join(map(str, reversed(digits + [carry]))).lstrip("0")
