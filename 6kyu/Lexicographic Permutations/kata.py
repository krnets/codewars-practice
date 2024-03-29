# def nth_perm(n, d):
#     digits = map(str, range(d))
#     # return "".join([*permutations(digits)][n - 1])
#     return "".join([*permutations(digits)][~-n])


# def permutations(iterable, r=None):
#     pool = tuple(iterable)
#     n = len(pool)
#     r = n if r is None else r
#     if r > n:
#         return
#     indices = [*range(n)]
#     cycles = [*range(n, n - r, -1)]
#     yield tuple(pool[i] for i in indices[:r])
#     while n:
#         for i in reversed(range(r)):
#             cycles[i] -= 1
#             if cycles[i] == 0:
#                 indices[i:] = indices[i + 1 :] + indices[i : i + 1]
#                 cycles[i] = n - i
#             else:
#                 j = cycles[i]
#                 indices[i], indices[-j] = indices[-j], indices[i]
#                 yield tuple(pool[i] for i in indices[:r])
#                 break
#         else:
#             return

from math import factorial


def nth_perm(n, d):
    factorials = [*map(factorial, range(d))]
    digits = [*map(str, range(d))]
    n -= 1
    for fct in reversed(factorials):
        i, n = divmod(n, fct)
        digits.append(digits.pop(i))
    return "".join(digits)
