from itertools import pairwise

# def divisible_by_last(n):
#     res = [False]
#     for x, y in pairwise(map(int, str(n))):
#         # if x and y % x == 0: res.append(True)
#         # else: res.append(False)
#         res.append(x and y % x == 0)
#     return res


# def divisible_by_last(n):
#     return [False] + [x and y % x == 0 for x, y in pairwise(map(int, str(n)))]


def divisible_by_last(n):
    return [False, *(x and y % x == 0 for x, y in pairwise(map(int, str(n))))]
