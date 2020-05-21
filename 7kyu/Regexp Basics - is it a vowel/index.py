# 7kyu - Regexp Basics - is it a vowel?

"""Implement the function which should return true if given object is a vowel 
(meaning a, e, i, o, u), and false otherwise."""

import re

def is_vowel(s):
    return bool(re.match('[aeiou]', s, re.I)) and len(s) == 1

q = is_vowel(""), False
q
q = is_vowel("a"), True
q
q = is_vowel("E"), True
q
q = is_vowel("ou"), False
q
q = is_vowel("z"), False
q
q = is_vowel("lol"), False
q
