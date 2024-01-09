# def two_highest(arg1):
#     if not arg1:
#         return arg1

#     vals = set(arg1)
#     max1 = max(vals)
#     vals.remove(max1)

#     if vals:
#         max2 = max(vals)
#         return [max1, max2]
#     else:
#         return [max1]

import heapq


def two_highest(arg1):
    return heapq.nlargest(2, set(arg1)) if arg1 else []
