# 6kyu - Split Strings

""" Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef'] """

import re

# def solution(s):
#     return [x if len(x) == 2 else x + '_' for x in re.findall(r'.{2}|.{1}', s)]

# def solution(s):
#     return re.findall('.{2}', s + '_')

def solution(s):
    return re.findall('..', s + '_')


q = solution("asdfadsf"), ['as', 'df', 'ad', 'sf']
q
q = solution("asdfads"), ['as', 'df', 'ad', 's_']
q
q = solution(""), []
q
q = solution("x"), ["x_"]
q
