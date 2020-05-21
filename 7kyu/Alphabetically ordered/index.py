# 7kyu - Alphabetically ordered

""" Your task is very simple. Just write a function alphabetic(s), which takes an input string s 
in lowercase and returns true/false depending on whether the string is in alphabetical order or not.

For example, alphabetic('kata') is False as 'a' comes after 'k', but alphabetic('ant') is True. """

# def alphabetic(s):
#     for i in range(len(s)-1):
#         if s[i] > s[i+1]:
#             return False
#     return True

def alphabetic(s):
    for i in range(1, len(s)):
        if s[i-1] > s[i]:
            return False
    return True

# def alphabetic(s):
#     return sorted(s) == list(s)

# def alphabetic(s):
#     return all(x <= y for x, y in (zip(s, s[1:])))


q = alphabetic('asd')  # False
q
q = alphabetic('codewars')  # False
q
q = alphabetic('door')  # True
q
q = alphabetic('cell')  # True
q
q = alphabetic('z')  # True
q
q = alphabetic('')  # True
q
