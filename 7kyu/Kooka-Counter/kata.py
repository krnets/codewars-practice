# def kooka_counter(laughing):
#     prev = ""
#     count = 0
#     for c in laughing[::2]:
#         if c != prev:
#             prev = c
#             count += 1
#     return count

import re


# def kooka_counter(laughing):
#     return len(re.findall(r"(ha)+|(Ha)+", laughing))


# def kooka_counter(laughing):
#     return len(re.findall(r"(ha|Ha)\1*", laughing))

from itertools import groupby


# def kooka_counter(laughing):
#     return len([*groupby(laughing.replace("a", ""))])


def kooka_counter(laughing):
    return len([*groupby(laughing[::2])])
