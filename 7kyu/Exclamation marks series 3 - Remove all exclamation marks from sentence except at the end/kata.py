# def remove(s):
#     pos = len(s) - 1
#     is_exclam = s[-1] == "!"
#     while pos and is_exclam:
#         if s[pos] == "!":
#             pos -= 1
#         else:
#             is_exclam = False
#     return s[:pos].replace("!", "") + s[pos:]

import re


def remove(s):
    return re.sub(r"!+(?=[^!])", "", s)
