from itertools import groupby
from operator import itemgetter


def longest_repetition(chars):
    repetitons = ((c, len(list(group))) for c, group in groupby(chars))
    return max(repetitons, key=itemgetter(1), default=("", 0))
