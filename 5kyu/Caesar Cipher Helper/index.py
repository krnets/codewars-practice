# 5kyu - Caesar Cipher Helper

""" Write a class that, when given a string, will return an uppercase string with each letter 
shifted forward in the alphabet by however many spots the cipher was initialized to.

For example:

c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES'

If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
The shift will always be in range of [1, 26]. """

from string import ascii_uppercase as ABC

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
        self.caesar = ABC.translate(str.maketrans(ABC, ABC[self.shift:] + ABC[:self.shift]))

    def encode(self, s):
        return s.upper().translate(str.maketrans(self.caesar, self.caesar[self.shift:] + self.caesar[:self.shift]))

    def decode(self, s):
        return s.translate(str.maketrans(self.caesar, self.caesar[-self.shift:] + self.caesar[:-self.shift]))



c = CaesarCipher(5)

q = c.encode('Codewars'), 'HTIJBFWX'
q
q = c.decode('HTIJBFWX'), 'CODEWARS'
q
