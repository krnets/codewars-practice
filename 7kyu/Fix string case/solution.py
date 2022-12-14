""" In this Kata, you will be given a string that may have mixed uppercase and lowercase letters 
and your task is to convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase."""


# def solve(s):
#     upper_count = sum(x.isupper() for x in s)
#     return s.lower() if upper_count <= len(s) // 2 else s.upper()


def solve(s):
    return s.upper() if sum(map(str.isupper, s)) * 2 > len(s) else s.lower()


q = solve("code")  # "code"
q
q = solve("CODe")  # "CODE"
q
q = solve("COde")  # "code"
q
q = solve("Code")  # "code"
q
