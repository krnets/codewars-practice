# def easyline(n):
#     res, aux = 0, 1
#     for i in range(n + 1):
#         res += aux * aux
#         aux = aux * (n - i) // (i + 1)
#     return res


# def easyline(n):
#     total, coef = 0, 1
#     for i in range(n + 1):
#         total += coef * coef
#         coef = coef * (n - i) // (i + 1)
#     return total


# def easyline(n):
#     return easyline(n - 1) * (4 * n - 2) // n if n else 1

# from math import comb


# def easyline(n):
#     return comb(2 * n, n)

from math import factorial


def easyline(n):
    return factorial(2 * n) // factorial(n) ** 2
