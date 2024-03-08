import re

def show_me(name):
    return bool(re.fullmatch(r"[A-Z][a-z]+(-[A-Z][a-z]+)*", name))
