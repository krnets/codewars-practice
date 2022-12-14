# 7kyu - Sum of Triangular Numbers

""" Your task is to return the sum of Triangular Numbers up-to-and-including the nth Triangular Number.

Triangular Number: "any of the series of numbers (1, 3, 6, 10, 15, etc.) obtained by continued summation 
of the natural numbers 1, 2, 3, 4, 5, etc."

[01]
02 [03]
04 05 [06]
07 08 09 [10]
11 12 13 14 [15]
16 17 18 19 20 [21]

e.g. If 4 is given: 1 + 3 + 6 + 10 = 20.

Triangular Numbers cannot be negative so return 0 if a negative number is given. """


# def sum_triangular_numbers(n):
#     triangular = []
#     for i in range(1, n+1):
#         triangular.append(i * (i + 1) // 2)
#     return sum(triangular)


# def sum_triangular_numbers(n):
#     cur = 0
#     ans = 0

#     for i in range(1, n + 1):
#         for j in range(cur, cur + i):
#             cur += 1
#         ans += cur

#     return 0 if n < 0 else ans


# def sum_triangular_numbers(n):
#     return sum(i * (i + 1) // 2 for i in range(n + 1))


# def sum_triangular_numbers(n):
#     return sum(i * (n - i + 1) for i in range(n + 1))


# def sum_triangular_numbers(n):
#     return max(0, n * (n + 1) * (n + 2) // 6)


def sum_triangular_numbers(n):
    return 0 if n < 0 else n * (n + 1) * (n + 2) // 6


q = sum_triangular_numbers(6)  # 56
q
q = sum_triangular_numbers(34)  # 7140
q
q = sum_triangular_numbers(-291)  # 0
q
q = sum_triangular_numbers(943)  # 140205240
q
q = sum_triangular_numbers(-971)  # 0
q
