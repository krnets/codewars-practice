# def keep_order(ary, val):
#     for i, x in enumerate(ary):
#         if x >= val:
#             return i
#     return len(ary)

from bisect import bisect_left


def keep_order(ary, val):
    return bisect_left(ary, val)
