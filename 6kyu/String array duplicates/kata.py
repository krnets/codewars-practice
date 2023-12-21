# def dup(arry):
#     res = []

#     for item in arry:
#         x = item[0]
#         for c in item[1:]:
#             if c != x[-1]:
#                 x += c
#         res.append(x)

#     return res

# from itertools import groupby


# def dup(arry):
#     return ["".join(c for c, _ in groupby(i)) for i in arry]

import re

def dup(arry):
    return [*map(lambda s: re.sub(r"(.)\1+", r"\1", s), arry)]
