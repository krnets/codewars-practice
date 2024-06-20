# def dup(arry):
#     res = []
#     for word in arry:
#         clean = word[0]
#         for c in word[1:]:
#             if c != clean[-1]:
#                 clean += c
#         res.append(clean)
#     return res

# from itertools import groupby

# def dup(arry):
#     return ["".join(k for k, _ in groupby(word)) for word in arry]


import re

def dup(arry):
    return [*map(lambda s: re.sub(r"(.)\1+", r"\1", s), arry)]
