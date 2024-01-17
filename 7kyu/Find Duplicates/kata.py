# def duplicates(arr):
#     res = []
#     seen = set()
#     for x in arr:
#         if x not in seen:
#             seen.add(x)
#         elif x not in res:
#             res.append(x)
#     return res

from collections import defaultdict


def duplicates(arr):
    res = []
    counter = defaultdict(int)
    for x in arr:
        counter[x] += 1
        if counter[x] == 2:
            res.append(x)
    return res
