# 6kyu - Count letters in string

""" In this kata, you've to count lowercase letters in a given string and return the letter count 
in a hash with 'letter' as key and count as 'value'. 

letter_count('arithmetics') #=> {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2} """

# from collections import Counter

# def letter_count(s):
#     return Counter(s)

from collections import Counter as letter_count

q = letter_count("codewars") # {"a": 1, "c": 1, "d": 1, "e": 1, "o": 1, "r": 1, "s": 1, "w": 1}
q
q = letter_count("activity") # {"a": 1, "c": 1, "i": 2, "t": 2, "v": 1, "y": 1}
q
q = letter_count("arithmetics") # {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}
q
q = letter_count("traveller") # {"a": 1, "e": 2, "l": 2, "r": 2, "t": 1, "v": 1}
q
q = letter_count("daydreamer") # {"a": 2, "d": 2, "e": 2, "m": 1, "r": 2, "y": 1}
q

