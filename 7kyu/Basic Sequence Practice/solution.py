# def sum_of_n(n):
#     res = []
#     is_neg = n < 0
#     m = abs(n) + 1
#     i = 1

#     while len(res) < m:
#         sum = i * (i - 1) // 2
#         res.append(-sum if is_neg else sum)
#         i += 1

#     return res

from itertools import accumulate


# def sum_of_n(n):
# return [*accumulate(range(0, *(n - 1, -1) if n < 0 else (n + 1, 1)))]


def sum_of_n(n):
    return [*accumulate(range(0, n - 1, -1) if n < 0 else range(n + 1))]


q = sum_of_n(3)  # [0, 1, 3, 6]
q
q = sum_of_n(-4)  # [0, -1, -3, -6, -10]
q
q = sum_of_n(1)  # [0, 1]
q
q = sum_of_n(0)  # [0]
q
q = sum_of_n(10)  # [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
q
