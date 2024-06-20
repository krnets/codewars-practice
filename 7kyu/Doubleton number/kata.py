# def doubleton(num):
#     for i in range(num + 1, 1_000_000):
#         if len(set(str(i))) == 2:
#             return i

from itertools import count


def doubleton(num):
    return next(n for n in count(num + 1) if len(set(str(n))) == 2)


# def doubleton(num):
#     return next(n for n in count(num + 1) if is_doubleton(n))


# def is_doubleton(n):
#     digits = set()
#     while n:
#         n, r = divmod(n, 10)
#         digits.add(r)
#     return len(digits) == 2
