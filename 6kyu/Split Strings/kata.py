# def solution(s):
#     if not s:
#         return []
#     res = [s[i : i + 2] for i in range(0, len(s), 2)]
#     if len(res[-1]) == 1:
#         res[-1] += "_"
#     return res


# def solution(s):
#     if len(s) & 1:
#         s += "_"
#     return [s[i : i + 2] for i in range(0, len(s), 2)]

import re


def solution(s):
    return re.findall("..", s + "_")
