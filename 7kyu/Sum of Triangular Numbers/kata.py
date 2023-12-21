# def sum_triangular_numbers(n):
#     if n < 1:
#         return 0

#     triangle, ans = 0, 0

#     for i in range(1, n + 1):
#         triangle += i
#         ans += triangle

#     return ans


# def sum_triangular_numbers(n):
#     return n * (n + 1) * (n + 2) // 6 if n > 0 else 0

from itertools import accumulate

def sum_triangular_numbers(n):
    return sum(accumulate(range(1, n + 1))) if n > 0 else 0
