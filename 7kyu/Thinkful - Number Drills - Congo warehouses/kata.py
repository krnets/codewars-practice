from math import prod


def box_capacity(*args):
    return prod(x * 12 // 16 for x in args)
