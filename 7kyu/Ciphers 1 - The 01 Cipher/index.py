""" 7kyu - Ciphers #1 - The 01 Cipher

Cipher looks at the letter, and sees it's index in the alphabet, the alphabet being a-z, if you didn't know. 
If it is odd, it is replaced with 1, if it's even, its replaced with 0. Note that the index should start from 0. 
If letter's index is odd, replaced with 1. If the character isn't a letter, it remains the same.  """

def encode(s):
    return ''.join(str(1 - ord(x) % 2) if x.isalpha() else x for x in s)


q = encode("Hello World!"), "10110 00111!"
q
