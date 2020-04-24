# 6kyu - Valid Braces

""" Write a function that takes a string of braces, and determines if the order of the braces is valid. 
It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: 
brackets [], and curly braces {}.

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: 
()[]{}.

What is considered Valid?

A string of braces is considered valid if all braces are matched with the correct brace.

"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False """


# def validBraces(string):
#     parentheses = []
#     square = []
#     braces = []
#     try:
#         for i in range(len(string)):
#             if string[i] == '(':
#                 parentheses.append(')')
#             elif string[i] == ')':
#                 parentheses.pop()
#             elif string[i] == '{':
#                 braces.append('{')
#             elif string[i] == '}':
#                 braces.pop()
#             elif string[i] == '[':
#                 square.append('[')
#             elif string[i] == ']':
#                 square.pop()
#     except:
#         return False

#     return len(parentheses) == 0 and len(braces) == 0 and len(square) == 0


import re

# def validBraces(string):
#     while re.findall('(\{\})|(\(\))|(\[\])', string):
#         string = re.sub('(\{\})|(\(\))|(\[\])', '', string)
#     return not string

def validBraces(string):
    while re.findall('\{\}|\(\)|\[\]', string):
        string = re.sub('\{\}|\(\)|\[\]', '', string)
    return not string



q = validBraces("()"), True
q
q = validBraces("[(])"), False
q
q = validBraces("(){}[]"), True
q
q = validBraces("([{}])"), True
q
q = validBraces("(}"), False
q
q = validBraces("[(])"), False
q
q = validBraces("[({})](]"), False
q
