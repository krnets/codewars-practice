""" 5kyu - Rot13

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters 
after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating. """

# def rot13(message):
#     a, A = ord('a'),  ord('A')
#     res = []
#     for x in message:
#         if a <= ord(x) <= a+26:
#             res.append(chr((ord(x)-a+13) % 26 + a))
#         elif A <= ord(x) <= A+26:
#             res.append(chr((ord(x)-A+13) % 26 + A))
#         else:
#             res.append(x)
#     return ''.join(res)

from string import ascii_lowercase as abc, ascii_uppercase as ABC

# def rot13(message):
#     res = []
#     abc_cipher = abc + abc
#     ABC_cipher = ABC + ABC
#     for x in message:
#         if x.islower():
#             res.append(abc_cipher[abc_cipher.index(x)+13])
#         elif x.isupper():
#             res.append(ABC_cipher[ABC_cipher.index(x)+13])
#         else:
#             res.append(x)
#     return ''.join(res)


def rot13(message):
    cipher = str.maketrans(abc+ABC, abc[13:]+abc[:13]+ABC[13:]+ABC[:13])
    return message.translate(cipher)

# import codecs

# def rot13(message):
#     return codecs.encode(message, 'rot13')


q = rot13("test"), "grfg"
q
q = rot13("Test"), "Grfg"
q
q = rot13("Test!"), "Grfg!"
q
