import re

# def remove_parentheses(st):
#     pattern = "\([^()]*\)"
#     while "(" in st:
#         st = re.sub(pattern, "", st)
#     return st


def remove_parentheses(st):
    pattern = "\([^()]*\)"
    while st != (subbed := re.sub(pattern, "", st)):
        st = subbed
    return st
