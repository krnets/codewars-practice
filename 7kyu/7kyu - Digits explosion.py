# 7kyu - Digits explosion

""" Given a string made of digits [0-9], return a string where each digit 
is repeated a number of times equals to its value.

Digits.Explode("312") = "333122"
Digits.Explode("102269") = "12222666666999999999" """


def explode(s):
    return ''.join(x * int(x) for x in s)

# import re

# def explode(s):
#     return re.sub('\d', lambda d: d.group() * int(d.group()), s)


q = explode("312"), "333122"
q
q = explode("102269"), "12222666666999999999"
q
q = explode("0"), ""
q
q = explode("000"), ""
q
q = explode("123"), "122333"
q
