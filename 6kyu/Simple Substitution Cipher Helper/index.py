""" 6kyu - Simple Substitution Cipher Helper

A simple substitution cipher replaces one character from an alphabet with a character 
from an alternate alphabet, where each character's position in an alphabet is 
mapped to the alternate alphabet for encoding or decoding.

map1 = "abcdefghijklmnopqrstuvwxyz";
map2 = "etaoinshrdlucmfwypvbgkjqxz";

cipher = Cipher(map1, map2);
cipher.encode("abc") # => "eta"
cipher.encode("xyz") # => "qxz"
cipher.encode("aeiou") # => "eirfg"

cipher.decode("eta") # => "abc"
cipher.decode("qxz") # => "xyz"
cipher.decode("eirfg") # => "aeiou"

If a character provided is not in the opposing alphabet, simply leave it as be. """


class Cipher(object):
    def __init__(self, map1, map2):
        self.encoder = str.maketrans(map1, map2)
        self.decoder = str.maketrans(map2, map1)

    def encode(self, s):
        return s.translate(self.encoder)

    def decode(self, s):
        return s.translate(self.decoder)


map1 = "abcdefghijklmnopqrstuvwxyz"
map2 = "etaoinshrdlucmfwypvbgkjqxz"

cipher = Cipher(map1, map2)
q = cipher.encode("abc"), "eta"
q
q = cipher.encode("xyz"), "qxz"
q
q = cipher.decode("eirfg"), "aeiou"
q
q = cipher.decode("erlang"), "aikcfu"
q

map2 = 'tfozcivbsjhengarudlkpwqxmy'
cipher = Cipher(map1, map2)
q = cipher.encode('abc'), 'tfo'
q
q = cipher.decode('tfo'), 'abc'
q
q = cipher.decode('kjpphi'), 'tjuukf'
q
q = cipher.encode('ajqqtb'), 'tjuukf'
q
