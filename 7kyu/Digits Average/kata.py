from itertools import pairwise
from math import ceil

# def digits_average(x):
#     while x > 9:
#         digits = [str(int(ceil((a + b) / 2))) for a, b in pairwise(map(int, str(x)))]
#         x = int("".join(digits))
#     return x


def digits_average(x):
    digits = [*map(int, str(x))]

    while len(digits) > 1:
        digits = [(a + b + 1) // 2 for a, b in pairwise(digits)]

    return digits[0]
