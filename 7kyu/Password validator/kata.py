import re


def password(string):
    pattern = r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.{8,})"
    return bool(re.match(pattern, string))
