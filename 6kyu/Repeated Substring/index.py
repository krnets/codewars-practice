""" 6kyu - Repeated Substring

For a given nonempty string s find a minimum substring t and the maximum number k, 
such that the entire string s is equal to t repeated k times. 
The input string consists of lowercase latin letters. 
Your function should return an array [t, k]  """

import re

# def f(s):
#     match = re.findall(r'(..*?)(?=\1*$)', s)
#     return [match[0], len(match)]

# def f(s):
#     match = re.findall(r'(.+?)\1*$', s)[0]
#     return match, len(s) / len(match)

def f(s):
    match = re.findall(r'(.+?)(?=\1*$)', s)
    return match[0], len(match)


q = f("ababab"), ("ab", 3)
q
q = f("abcde"), ("abcde", 1)
q
