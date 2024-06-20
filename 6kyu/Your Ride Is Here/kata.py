from math import prod


def ride(group, comet):
    prod_group = prod(chars_to_ints(group))
    prod_comet = prod(chars_to_ints(comet))
    return ("STAY", "GO")[prod_group % 47 == prod_comet % 47]


def chars_to_ints(comet_name):
    offset = ord("A") - 1
    return (ord(c) - offset for c in comet_name)
