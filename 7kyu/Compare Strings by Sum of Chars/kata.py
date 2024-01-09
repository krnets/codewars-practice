import re


def compare(s1, s2):
    if not s1 or bool(re.findall(r"[^a-z]", s1, re.IGNORECASE)):
        s1 = ""
    if not s2 or bool(re.findall(r"[^a-z]", s2, re.IGNORECASE)):
        s2 = ""
    return sum(map(ord, s1.lower())) == sum(map(ord, s2.lower()))
