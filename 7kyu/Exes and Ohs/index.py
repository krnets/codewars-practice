# 7kyu - Exes and Ohs

""" Check to see if a string has the same amount of 'x's and 'o's. 
The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false """


# def xo(s):
#     balance = 0
#     for c in s.lower():
#         if c == 'x':
#             balance += 1
#         elif c == 'o':
#             balance -= 1
#     return balance == 0

# def xo(s):
#     s = s.lower()
#     return s.count('x') == s.count('o')

# def xo(s):
#     return sum(1 if c == 'x' else -1 if c == 'o' else 0 for c in s.lower()) == 0

from collections import Counter

def xo(s):
    freq = Counter(s.lower())
    # return freq.get('x', 0) == freq.get('o', 0)
    return freq['x'] == freq['0']


q = xo("xo")  # True
q
q = xo("xo0")  # True
q
q = xo("xxxoo")  # False
q
