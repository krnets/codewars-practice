# 7kyu - Isograms

""" An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case """

# from collections import Counter

# def is_isogram(string):
#     freq = Counter(string.lower())
#     return all(x == 1 for x in freq.values())

# def is_isogram(string):
#     s = string.lower()
#     return len([x for x in Counter(s).values() if x != 1]) == 0

# def is_isogram(string):
#     return len(set(string.lower())) == len(string)


def is_isogram(string):
    return len(string) == len(set(string.lower()))

q = is_isogram("Dermatoglyphics")  # True
q
q = is_isogram("isogram")  # True
q
q = is_isogram("aba")  # False, "same chars may not be adjacent"
q
q = is_isogram("moOse")  # False, "same chars may not be same case"
q
q = is_isogram("isIsogram")  # False
q
q = is_isogram("")  # True, "an empty string is a valid isogram"
q
