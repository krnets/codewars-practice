# Beta - Hail Caesar

""" You are in the ancient Roman army and are Caesar's trusted companion and military advisor. 
He confides in you about numerous plots he has thwarted to take his life and tasks you to devise 
a way to keep secrets secret from his enemies.

You begin by creating a shift cipher, where the values of the letters get shifted by a specified (input) degree.

(exit story arc: A modern case of a shift cipher is the ROT13 cipher. 
The values of the letters are shifted by 13 places;'A' to 'N', and 'B' ↔ to'O'.

Create a function which takes a ROT13 encoded string as input and outputs a decoded string.

All letters are uppercase. Don't transform any non-alphabetic characters like spaces or punctuation, 
but do pass them on to the output. """


# from string import ascii_uppercase as ABC

# def hail_caesar(enc_str):
#     return enc_str.translate(str.maketrans(ABC, ABC[13:] + ABC[:13]))

import codecs

def hail_caesar(enc_str):
    return codecs.encode(enc_str, 'rot13')

# import this

# def hail_caesar(s):
#     return ''.join(this.d.get(c, c) for c in s)


encoded = "GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK."
decoded = "THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX."

q = hail_caesar(encoded)
q
