# def shifted_diff(first, second):
#     if first == second:
#         return 0
#     n = len(first)
#     for i in range(1, n):
#         if first[-i:] + first[: n - i] == second:
#             return i
#     return -1


# eecoff  0  coffee
# feecof  1  offeec
# ffeeco  2  ffeeco
# offeec  3  feecof
# coffee  4  eecoff


# def shifted_diff(first, second):
#     for i in range(len(first)):
#         if first == second[i:] + second[:i]:
#             return i
#     return -1


# def shifted_diff(first, second):
#     return (second * 2).find(first) if len(first) == len(second) else -1


def shifted_diff(first, second):
    return next((i for i in range(len(first)) if first == second[i:] + second[:i]), -1)
