from itertools import chain


# def pascals_triangle(n):
#     levels = []
#     for i in range(1, n + 1):
#         level = [0] * i
#         level[0] = 1
#         level[-1] = 1
#         for j in range(1, i - 1):
#             level[j] = levels[i - 2][j - 1] + levels[i - 2][j]
#         levels.append(level)
#     return [*chain.from_iterable(levels)]


def pascals_triangle(n):
    rows = []
    for i in range(n):
        row = [0] * (i + 1)
        row[0] = 1
        row[-1] = 1
        for j in range(1, i):
            row[j] = rows[i - 1][j - 1] + rows[i - 1][j]
        rows.append(row)
    return [*chain.from_iterable(rows)]


# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]

# from math import comb


# def pascals_triangle(n):
#     return [comb(m, k) for m in range(n) for k in range(m + 1)]
