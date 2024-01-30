# def solution(s):
#     last, res = 0, ""
#     for i in range(1, len(s)):
#         if "A" <= s[i] <= "Z":
#             res += s[last:i] + " "
#             last = i
#     return res + s[last : len(s)]


# def solution(s):
#     return "".join(" " + c if c.isupper() else c for c in s)

import re


def solution(s):
    return re.sub(r"([A-Z])", r" \1", s)
