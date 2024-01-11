# def string_merge(string1, string2, letter):
#     i = string1.index(letter)
#     j = string2.index(letter)
#     return string1[:i] + string2[j:]

from itertools import chain, dropwhile, takewhile


# def string_merge(string1, string2, letter):
#     return "".join(
#         chain(takewhile(letter.__ne__, string1),
#               dropwhile(letter.__ne__, string2)))


def string_merge(string1, string2, letter):
    return string1.partition(letter)[0] + letter + string2.partition(letter)[2]
