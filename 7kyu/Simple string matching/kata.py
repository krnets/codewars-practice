from fnmatch import fnmatch
import re

# def solve(a, b):
#     return bool(re.compile(a.replace("*", ".*")).fullmatch(b))


# def solve(a, b):
#     return bool(re.fullmatch(a.replace("*", ".*"), b))


def solve(a, b):
    return fnmatch(b, a)
