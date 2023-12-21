# def reverse_words(text):
#     ans = ""
#     word = ""
#     space = ""
#     for c in text:
#         if c == " ":
#             space += c
#             if word != "":
#                 ans += word[::-1]
#             word = ""
#         else:
#             if space != "":
#                 ans += space
#             space = ""
#             word += c

#     return ans + word[::-1]

import re

def reverse_words(text):
    return re.sub(r"\S+", lambda m: m.group()[::-1], text)
