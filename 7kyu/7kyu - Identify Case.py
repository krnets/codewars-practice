# 7kyu - Identify Case

""" We’ve all seen katas that ask for conversion from snake-case to camel-case, 
from camel-case to snake-case, or from camel-case to kebab-case — the possibilities are endless.

But if we don’t know the case our inputs are in, these are not very helpful.

So the task here is to implement a function case_id in Python that takes a string, c_str, 
and returns a string with the case the input is in. 
The possible case types are “kebab”, “camel”, and ”snake”. 
If none of the cases match with the input, or if there are no 'spaces' in the input 
(for example in snake case, spaces would be '_'s), return “none”. 
Inputs will only have letters (no numbers or special characters).

Kebab case: lowercase-words-separated-by-hyphens
Camel case: lowercaseFirstWordFollowedByCapitalizedWords
Snake case: lowercase_words_separated_by_underscores. """

import re

# def case_id(c_str):
#     if re.search('[a-z]-[a-z]', c_str):
#         return 'kebab'
#     if re.search('[a-z]_[a-z]', c_str):
#         return 'snake'
#     if all(x.lower() == x for x in c_str):
#         return 'none'
#     if re.search('^[a-zA-Z]+$', c_str):
#         return 'camel'
#     return 'none'

# CASES = [
#     ('snake', re.compile(r'\A[a-z]+(_[a-z]+)+\Z')),
#     ('kebab', re.compile(r'\A[a-z]+(-[a-z]+)+\Z')),
#     ('camel', re.compile(r'\A[a-z]+([A-Z][a-z]*)+\Z')),
#     ('none', re.compile(r'')),
# ]

CASES = [
    ('snake', re.compile('^[a-z]+(_[a-z]+)+$')),
    ('kebab', re.compile('^[a-z]+(-[a-z]+)+$')),
    ('camel', re.compile('^[a-z]+([A-Z][a-z]*)+$')),
    ('none', re.compile('')),
]

def case_id(c_str):
    for case, pattern in CASES:
        if pattern.match(c_str):
            return case


q = case_id(
    'uzbcok-ylxkwqape_AzpuficthqAZBmtskeagwfAZBhsaleqkgo--vybwpz--fohlAcfqlgxy')  # none
q
q = case_id('qisoA-baifdA-fbiwdh__kqig')  # none
q
q = case_id("hello-world")  # => “kebab”
q
q = case_id("hello-to-the-world")  # => “kebab”
q
q = case_id("helloWorld")  # => “camel”
q
q = case_id("helloToTheWorld")  # => “camel”
q
q = case_id("hello_world")  # => “snake”
q
q = case_id("hello_to_the_world")  # => “snake”
q
q = case_id("hello__world")  # => “none”
q
q = case_id("hello_World")  # => “none”
q
q = case_id("helloworld")  # => “none”
q
q = case_id("hello-World")  # => “none”
q
