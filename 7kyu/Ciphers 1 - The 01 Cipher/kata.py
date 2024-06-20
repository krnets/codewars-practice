# def encode(s):
#     res = ""

#     for c in s:
#         if c.isalpha():
#             res += ("1", "0")[ord(c) & 1]
#         else:
#             res += c

#     return res


# def encode(s):
#     return "".join(("1", "0")[ord(c) & 1] if c.isalpha() else c for c in s)


# def encode(s):
#     return "".join("10"[ord(c) & 1] if c.isalpha() else c for c in s)


# def encode(s):
#     return "".join(str(ord(c) & 1 ^ 1) if c.isalpha() else c for c in s)


# def encode(s):
#     return "".join(str(~ord(c) & 1) if c.isalpha() else c for c in s)

from string import ascii_letters as abc

CIPHER = str.maketrans(abc[::2] + abc[1::2], "0" * 26 + "1" * 26)
encode = lambda s: s.translate(CIPHER)
