""" 6kyu - Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

    Your message is a string containing space separated words.
    You need to encrypt each word in the message using the following rules:
        The first letter needs to be converted to its ASCII code.
        The second letter needs to be switched with the last letter
    Keepin' it simple: There are no special characters in input.

Examples:

encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo" """

import re

# def encrypt_this(text):
#     words = text.split()
#     for i in range(len(words)):
#         words[i] = re.sub(r'^(.)(.)(.*)(.)$', r'\1\4\3\2', words[i])
#         words[i] = str(ord(words[i][0])) + words[i][1:]
#     return ' '.join(words)


def encrypt_this(text):
    return ' '.join(str(ord(x[0]))+x[1:] for x in map(lambda w: re.sub(r'^(.)(.)(.*)(.)$', r'\1\4\3\2', w), text.split()))


q = encrypt_this(""), ""
q
q = encrypt_this("A wise old owl lived in an oak")
q
#     "65 119esi 111dl 111lw 108dvei 105n 97n 111ka"
q = encrypt_this("The more he saw the less he spoke")
q
#     "84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"
q = encrypt_this("The less he spoke the more he heard")
q
#     "84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"
q = encrypt_this("Why can we not all be like that wise old bird")
q
#     "87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"
q = encrypt_this("Thank you Piotr for all your help")
q
#     "84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"
