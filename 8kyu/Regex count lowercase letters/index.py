# 8kyu - Regex count lowercase letters

""" Your task is simply to count the total number of lowercase letters in a string. """

import re

def lowercase_count(string):
    return len(re.findall('[a-z]', string))

# def lowercase_count(string):
#     return sum([x.islower() for x in string])

# def lowercase_count(string):
#     return sum(1 for c in string if c.islower())


q = lowercase_count("abc")  # 3
q
q = lowercase_count("abcABC123")  # 3
q
q = lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~")  # 3
q
q = lowercase_count("")  # 0
q
q = lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~")  # 0
q
q = lowercase_count("abcdefghijklmnopqrstuvwxyz")  # 26
q
