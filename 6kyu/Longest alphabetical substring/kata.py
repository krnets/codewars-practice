# def longest(st):
#     i, prev, res = 0, 256, ""

#     for j, c in enumerate(st):
#         if prev > ord(c):
#             if j - i > len(res):
#                 res = st[i:j]
#             i = j
#         prev = ord(c)

#     if len(res) < len(st) - i:
#         res = st[i:]
#     return res

import re
from string import ascii_lowercase as abc


def longest(st):
    return max(re.findall(r"*".join(abc) + "*", st), key=len)
