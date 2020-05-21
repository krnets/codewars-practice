# 8kyu - Regexp Basics - is it a digit?


""" Implement is_digit which should return true if given object is a digit (0-9), false otherwise. """

import re

# def is_digit(n):
#     return bool(re.match('^\d$', n)) and len(n) == 1

def is_digit(n):
    return bool(re.match('\d\Z', n))

q = is_digit(""), False
q
q = is_digit("7"), True
q
q = is_digit(" "), False
q
q = is_digit("a"), False
q
q = is_digit("a5"), False
q
