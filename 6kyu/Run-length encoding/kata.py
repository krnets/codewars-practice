from itertools import groupby
import re


# def run_length_encoding(s):
#     return [[len(list(group)), c] for c, group in groupby(s)]


def run_length_encoding(s):
    return [[len(group), c] for group, c in re.findall(r"((.)\2*)", s)]
