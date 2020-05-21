# Beta - Count consecutive characters

""" Given a string, return a new string built by concatenating a sequence 'num+char' 
where 'num' is an integer that counts how many times the character 'char' appears consecutively in the original string.

Assumptions:
the string is nonempty;
the string is case sensitive (a != A).

Note that whitespaces are counted just like any other character. """

# from itertools import groupby

# def count_consecutives(s):
#     res = [''.join((str(len(list(g))), k)) for k, g in groupby(s)]
#     return ''.join(res)

# def count_consecutives(s):
#     return ''.join(str(sum(1 for _ in g)) + k for k, g in groupby(s))

import re

def count_consecutives(s):
    return re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)


q = count_consecutives('a')  # '1a'
q
q = count_consecutives('aaaa')  # '4a'
q
q = count_consecutives('aaabbccc')  # '3a2b3c'
q
q = count_consecutives('aaaAAAAb')  # '3a4A1b'
q
q = count_consecutives('ababab')  # '1a1b1a1b1a1b'
q
q = count_consecutives('aaa22bc3ddD')  # '3a221b1c132d1D'
q
q = count_consecutives('aa bb')  # '2a1 2b'
q
q = count_consecutives('aa aAab BbCcc   cZ')  # '2a1 1a1A1a1b1 1B1b1C2c3 1c1Z'
q
q = count_consecutives('annie mommy dummy ')
q
#     '1a2n1i1e1 1m1o2m1y1 1d1u2m1y1 '
