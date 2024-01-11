from collections import Counter


# def sum_no_duplicates(l):
#     ans = 0

#     for k, v in Counter(l).items():
#         if v == 1:
#             ans += k

#     return ans


def sum_no_duplicates(l):
    return sum(k for k, v in Counter(l).items() if v == 1)
