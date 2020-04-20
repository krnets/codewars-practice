# 6kyu - Alpha to Numeric and Numeric to Alpha

""" In this Kata, you will create a function that converts a string with letters and numbers 
to the inverse of that string (with regards to Alpha and Numeric characters). 
So, e.g. the letter a will become 1 and number 1 will become a; z will become 26 and 26 will become z.

Example: "a25bz" would become "1y226"

Numbers representing letters (n <= 26) will always be separated by letters, for all test cases:

    "a26b" may be tested, but not "a262b"
    "cjw9k" may be tested, but not "cjw99k"

A list named alphabet is preloaded for you: ['a', 'b', 'c', ...]

A dictionary of letters and their number equivalent is also preloaded for you called 
alphabetnums = {'a': '1', 'b': '2', 'c': '3', ...} """

from string import ascii_lowercase as abc
import re

alphabet = list(abc)
alphabetnums = {c: str(abc.index(c)+1) for c in abc}


# def AlphaNum_NumAlpha(string):
#     res = ''
#     for x in re.findall(r'\d+|\D', string):
#         if x.isdigit():
#             res += alphabet[int(x)-1]
#         else:
#             res += str(int(alphabetnums[x])+1)
#     return res

def AlphaNum_NumAlpha(string):
    return ''.join(alphabet[int(x)-1] if x.isdigit() else str(int(alphabetnums[x])) for x in re.findall(r'\d+|\D', string))


q = AlphaNum_NumAlpha('25abcd26')  # 'y1234z'
q
q = AlphaNum_NumAlpha('18zyz14')  # 'r262526n'
q
q = AlphaNum_NumAlpha('a1b2c3d4')  # '1a2b3c4d'
q
q = AlphaNum_NumAlpha('5a8p17')  # 'e1h16q'
q
