# def inside_out(st):
#     res = []

#     for word in st.split():
#         n = len(word)
#         if n < 4:
#             res.append(word)
#         else:
#             mid = n // 2
#             new_word = word[:mid][::-1] + ("", word[mid])[n & 1] + word[-mid:][::-1]
#             res.append(new_word)

#     return " ".join(res)

import re


def inside_out(st):
    return re.sub(r"\w{4,}", lambda m: process(m.group()), st)


def process(word):
    mid = len(word) // 2
    return word[:mid][::-1] + ("", word[mid])[len(word) & 1] + word[-mid:][::-1]
