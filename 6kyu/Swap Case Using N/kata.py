# def swap(s, n):
#     num_bin = f"{n:b}" * len(s)
#     t = (c for c in s if c.isalpha())
#     swapped = iter((c, c.swapcase())[num_bin[i] == "1"] for i, c in enumerate(t))
#     return "".join(next(swapped) if c.isalpha() else c for c in s)

from itertools import cycle


def swap(s, n):
    binary = cycle(map(int, f"{n:b}"))
    # return "".join(c.swapcase() if c.isalpha() and next(binary) else c for c in s)
    return "".join((c, c.swapcase())[c.isalpha() and next(binary)] for c in s)
