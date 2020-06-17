""" Beta - Encrypting words

Given a word in lowercase always you must to encrypt it.

To encrypt the word, is simple, replace the position of first character in the alphabet A-Z 
to the position of last character less position of first character.

For example in word hello:

h has position 7, z has position 25 => 25-7 = position 18

You must replace h for s, you make this task with every character in word.

hello -> svool cats -> xzgh

every character in lowercase. """

from string import ascii_lowercase as abc

# def encrypt(s):
#     return ''.join(abc[25 - abc.index(c)] for c in s)

def encrypt(s):
    return s.translate(str.maketrans(abc, abc[::-1]))


q = encrypt("hello"), "svool"
q
q = encrypt("cats"), "xzgh"
q
q = encrypt("dogs"), "wlth"
q
