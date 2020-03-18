# 7kyu - Ordered Count of Characters

""" Count the number of occurrences of each character and return it as a list of tuples in order of appearance.

ordered_count("abracadabra") == [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)] """

from collections import Counter

def ordered_count(input):
    return list(Counter(input).items())


q = ordered_count('abracadabra')
q
# [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)])
q = ordered_count('Code Wars')
q
# [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)])
