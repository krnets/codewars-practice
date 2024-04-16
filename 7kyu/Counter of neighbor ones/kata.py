# def ones_counter(inp):
#     return [len(s) for s in "".join(map(str, inp)).split("0") if s]

from itertools import groupby

def ones_counter(inp):
    return [sum(g) for k, g in groupby(inp) if k]
