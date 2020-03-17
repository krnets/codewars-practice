# 6kyu - One down

""" A very passive-aggressive co-worker of yours was just fired. 
While he was gathering his things, he quickly inserted a bug into your system which renamed everything to what looks like jibberish. 

He left two notes on his desk, one reads: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" 
while the other reads: "Uif usjdl up uijt lbub jt tjnqmf kvtu sfqmbdf fwfsz mfuufs xjui uif mfuufs uibu dpnft cfgpsf ju".

Rather than spending hours trying to find the bug itself, you decide to try and decode it.

If the input is not a string, your function must return "Input is not a string". 
Your function must be able to handle capital and lower case letters. 
You will not need to worry about punctuation. """

# import string
# import re

# def one_down(txt):
#     if not isinstance(txt, str):
#         return 'Input is not a string'
#     res = ''
#     s = string.ascii_uppercase + string.ascii_lowercase
#     for x in txt:
#         if x.isalpha():
#             res += s[s.index(x) - 1]
#         else:
#             res += x
#     return res


# def one_down(txt):
#     if not isinstance(txt, str):
#         return 'Input is not a string'
#     abc = string.ascii_lowercase
#     ABC = string.ascii_uppercase
#     text = re.sub(r'[a-z]', lambda m: abc[abc.index(m.group(0)) - 1], txt)
#     return re.sub(r'[A-Z]', lambda m: ABC[ABC.index(m.group(0)) - 1], text)

# import string

# def one_down(txt):
#     abc = string.ascii_lowercase
#     ABC = string.ascii_uppercase
#     transtab = str.maketrans(abc[1:] + abc[0] + ABC[1:] + ABC[0], abc + ABC)
#     return 'Input is not a string' if not isinstance(txt, str) else txt.translate(transtab)

from string import ascii_lowercase as abc
from string import ascii_uppercase as ABC

def one_down(txt):
    transtab = str.maketrans(abc[1:] + abc[0] + ABC[1:] + ABC[0], abc + ABC)
    return 'Input is not a string' if not isinstance(txt, str) else txt.translate(transtab)


q = one_down('A')
q
q = one_down("Ifmmp")  # "Hello"
q
q = one_down("Uif usjdl up uijt lbub jt tjnqmf")
q
# "The trick to this kata is simple"
q = one_down(45)  # "Input is not a string"
q
q = one_down("XiBu BcPvU dSbAz UfYu")  # "WhAt AbOuT cRaZy TeXt"
q
q = one_down(["Hello there", "World"])  # "Input is not a string"
q
q = one_down('PZZIvJhaUYWaNgHxy:CwxWjF')  # 'OYYHuIgzTXVzMfGwx:BvwViE'
q
