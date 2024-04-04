import re


# def connotation(strng):
#     positives = [bool(re.match("^[a-m]", x, re.I)) for x in strng.split()]
#     count_positives = sum(positives)
#     return count_positives >= len(positives) - count_positives


def connotation(strng):
    return sum([-1, 1][word[0] < "n"] for word in strng.lower().split()) >= 0
