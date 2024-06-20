# def has_subpattern(strng):
#     n = len(strng)

#     for i in range(1, n // 2):
#         candidate = strng[:i]
#         if strng == candidate * (n // i):
#             return True
#     return False


import re

def has_subpattern(strng):
    return bool(re.fullmatch(r"(.+)\1+", strng))


# def has_subpattern(strng):
#     return (strng * 2).find(strng, 1) != len(strng)
