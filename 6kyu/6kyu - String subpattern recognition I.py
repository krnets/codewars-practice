# 6kyu - String subpattern recognition I

""" In this kata you need to build a function to return either true/True or 
false/False if a string can be seen as the repetition of a simpler/shorter subpattern or not.

For example:

has_subpattern("a") == False #no repeated pattern
has_subpattern("aaaa") == True #created repeating "a"
has_subpattern("abcd") == False #no repeated pattern
has_subpattern("abababab") == True #created repeating "ab"
has_subpattern("ababababa") == False #cannot be entirely reproduced repeating a pattern

Strings will never be empty and can be composed of any character 
(just consider upper- and lowercase letters as different entities) 
and can be pretty long (keep an eye on performances!). """

# from collections import Counter
# from functools import reduce
# from fractions import gcd

# def has_subpattern(string):
#     c = Counter(string)
#     m = reduce(gcd, c.values())
#     res = [k * (v // m) for k, v in c.items()]
#     return m > 1 and len(res) is not m

# def has_subpattern(string):
#     n = len(string)
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             q = n // i
#             if string[:i] * q == string:
#                 return True
#     return False

def has_subpattern(string):
    return string in (2 * string)[1:-1]

# def has_subpattern(string):
#     return (string * 2).find(string, 1) != len(string)

# import re

# def has_subpattern(s):
#     return bool(re.search(r'^(.+)\1+$', s))

# def has_subpattern(string):
#     return bool(re.match(r'(.+)\1+$', string))

q = has_subpattern("a")  # False
q
q = has_subpattern("aaaa")  # True
q
q = has_subpattern("abcd")  # False
q
q = has_subpattern("abababab")  # True
q
q = has_subpattern("ababababa")  # False
q
q = has_subpattern("123a123a123a")  # True
q
q = has_subpattern("123A123a123a")  # False
q
q = has_subpattern("abbaabbaabba")  # True
q
q = has_subpattern("abbabbabba")  # False
q
q = has_subpattern("abcdabcabcd")  # False
q
