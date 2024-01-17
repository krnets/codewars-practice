from itertools import pairwise

# def catch_sign_change(lst):
#     return sum(x < 0 and y >= 0 or y < 0 and x >= 0 for x, y in pairwise(lst))


def catch_sign_change(lst):
    return sum((x < 0) is not (y < 0) for x, y in pairwise(lst))
