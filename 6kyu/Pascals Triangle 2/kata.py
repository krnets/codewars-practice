# def pascal(p):
#     triangle = [[1]]

#     for i in range(1, p):
#         inner = [0] * (i + 1)
#         inner[0] = inner[-1] = 1

#         for j in range(1, i):
#             inner[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

#         triangle.append(inner)

#     return triangle

from itertools import pairwise


def pascal(p):
    triangle = [[1]]

    for _ in range(1, p):
        row = [1, *map(sum, pairwise(triangle[-1])), 1]
        triangle.append(row)

    return triangle
