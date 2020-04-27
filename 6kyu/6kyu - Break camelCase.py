# 6kyu - Break camelCase

""" Complete the solution so that the function will break up camel casing, using a space between words.

solution("camelCasing")  ==  "camel Casing" """

import re

def solution(s):
    return re.sub(r'([A-Z])', r' \1', s)

# def solution(s):
#     return ''.join(' ' + x if x.isupper() else x for x in s)


q = solution("helloWorld")  # "hello World"
q
q = solution("camelCase")  # "camel Case"
q
q = solution("breakCamelCase")  # "break Camel Case"
q
