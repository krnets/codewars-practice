# def kebabize(st):
#     prev_char = st[0]
#     res = ("", prev_char)[prev_char.isalpha()]

#     for c in st[1:]:
#         if c.isalpha():
#             if c.isupper():
#                 res += "-"
#             res += c
#             prev_char = c

#     return res.lower().lstrip("-")


# def kebabize(st):
#     return "".join(c if c.islower() else "-" + c.lower() for c in st if c.isalpha()).lstrip("-")

import re

def kebabize(st):
    return re.sub(r"\B([A-Z])", r"-\1", re.sub("\d", "", st)).lower()
