# def solve(s):
#     letters = s.replace(" ", "")
#     i = len(letters) - 1
#     res = ""

#     for c in s:
#         if c == " ":
#             res += c
#         else:
#             res += letters[i]
#             i -= 1

#     return res


# def solve(s):
#     i = len(s) - 1
#     res = ""

#     for c in s:
#         if c == " ":
#             res += c
#         else:
#             if s[i] == " ":
#                 i -= 1
#             res += s[i]
#             i -= 1

#     return res


def solve(s):
    it = reversed(s.replace(" ", ""))
    return "".join(c if c == " " else next(it) for c in s)
