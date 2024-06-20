from itertools import chain


def array_mash(a, b):
    return [*chain.from_iterable(zip(a, b))]
