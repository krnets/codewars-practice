import re


def hydrate(drink_string):
    water = sum(map(int, re.findall(r"\d+", drink_string)))
    return f"{water} glass{'es' if water > 1 else ''} of water"
