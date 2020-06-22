""" 6kyu - regex pattern to check if string has all characters

Your function should return a valid regular expression. 
This is a pattern which is normally used to match parts of a string. 
In this case will be used to check if all the characters given in the input appear in a string.

Input: Non empty string of unique alphabet characters upper and lower case.
Output: Regular expression pattern string.


# Function example
def regex_contains_all(st): 
  return r"abc"

That regex pattern will be tested like this.

# Test
abc = 'abc'
pattern = regex_contains_all(abc)
st = 'zzzaaacccbbbzzz'
bool(re.match(pattern, st), f"Testing if {st} contains all characters in {abc} with your pattern {pattern}") -> True """

import re

# def regex_contains_all(st):
#     return ''.join(f"(?=.*{x})" for x in st)


def regex_contains_all(st):
    return ''.join(f"(?=.*{x})" for x in set(st))


abc = 'abc'
pattern = regex_contains_all(abc)

q = regex_contains_all(abc)
q

q = bool(re.match(pattern, 'bca')), True
q
q = bool(re.match(pattern, 'baczzz')), True
q
q = bool(re.match(pattern, 'ac')), False
q
q = bool(re.match(pattern, 'bc')), False
q
q = bool(re.match(pattern, 'cb')), False
q
