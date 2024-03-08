from itertools import chain


# def square_up(n):
#     res = []

#     for i in range(n):
#         sub = [*range(1, n + 1)]
#         for j in range(i):
#             sub[-j - 1] = 0
#         res.append(sub)

#     return [*chain.from_iterable(res)][::-1]


# def square_up(n):
#     res = []
#     for i in range(1, n + 1):
#         res.extend([0] * (n - i) + [*range(i, 0, -1)])
#     return res


def square_up(n):
    return [*chain.from_iterable([0] * (n - i) + [*range(i, 0, -1)] for i in range(1, n + 1)) ]
