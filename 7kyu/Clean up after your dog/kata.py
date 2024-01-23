# def crap(garden, bags, cap):
#     if any("D" in row for row in garden):
#         return "Dog!!"
#     return "Clean" if sum(1 for row in garden for x in row if x == "@") <= bags * cap else "Cr@p"

from collections import Counter
from itertools import chain


def crap(garden, bags, cap):
    freq = Counter(chain(*garden))
    return "Dog!!" if freq["D"] else ("Clean", "Cr@p")[freq["@"] > bags * cap]
