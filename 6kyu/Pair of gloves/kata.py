from collections import Counter
from itertools import groupby

# def number_of_pairs(gloves):
#     return sum(count // 2 for count in Counter(gloves).values())

def number_of_pairs(gloves):
    return sum(len([*group]) // 2 for _, group in groupby(sorted(gloves)))