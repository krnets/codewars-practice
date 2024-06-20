from itertools import pairwise
import re

# def comes_after(st, l):
#     return "".join(d for c, d in pairwise(st) if c.lower() == l.lower() and d.isalpha())


def comes_after(st, l):
    return "".join(re.findall(rf"(?i)(?<={l})([a-z])", st))
