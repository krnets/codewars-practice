import re


# def compare(s1, s2):
#     if isinstance(s1, list) or isinstance(s2, list):
#         return False
#     if not s1 or bool(re.findall(r"[^a-z]", s1, re.IGNORECASE)):
#         s1 = ""
#     if not s2 or bool(re.findall(r"[^a-z]", s2, re.IGNORECASE)):
#         s2 = ""
#     return sum(map(ord, s1.upper())) == sum(map(ord, s2.upper()))


def compare(s1, s2):
    if isinstance(s1, list) or isinstance(s2, list):
        return False
    if not s1 or not s1.isalpha():
        s1 = ""
    if not s2 or not s2.isalpha():
        s2 = ""
    return sum(map(ord, s1.upper())) == sum(map(ord, s2.upper()))
