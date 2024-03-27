# def thirt(n):
#     pattern = [1, 10, 9, 12, 3, 4]
#     res, i, p, m = 0, 0, n, len(pattern)

#     while p:
#         res += (p % 10) * pattern[i % m]
#         p //= 10
#         i += 1

#     return res if res == n else thirt(res)

from itertools import cycle


def thirt(n):
    pattern = cycle([1, 10, 9, 12, 3, 4])
    res, m = 0, n

    while m:
        res += (m % 10) * next(pattern)
        m //= 10

    return res if res == n else thirt(res)
