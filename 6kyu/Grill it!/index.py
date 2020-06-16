""" 6kyu - Grill it!

A grille cipher was a technique for encrypting a plaintext by writing it onto a sheet of paper through 
a pierced sheet (of paper or cardboard or similar). The earliest known description is due to the polymath 
Girolamo Cardano in 1550. His proposal was for a rectangular stencil allowing single letters, syllables, 
or words to be written, then later read, through its various apertures. The written fragments of the 
plaintext could be further disguised by filling the gaps between the fragments with anodyne words or letters. 
This variant is also an example of steganography, as are many of the grille ciphers. 

Task

Write a function that accepts two inputs: message and code and returns hidden message decrypted from 
message using the code. The code is a nonnegative integer and it decrypts in binary the message.

Grille("abcdef", 5)  => "df"

message : abcdef
code    : 000101
----------------
result  : df  """


# def grille(message, code):
#     n = len(message) if len(message) < code else code
#     return ''.join(y for x, y in zip(bin(code)[2:].zfill(n)[-n:], message[-n:]) if x == '1')

def grille(message, code):
    return ''.join(m for m, c in zip(message[::-1], f'{code:b}'[::-1]) if c == '1')[::-1]


q = grille("", 5), ""
q

q = grille("abcd", 1), "d"
q
q = grille("0abc", 2), "b"
q
q = grille("ab", 255), "ab"
q
q = grille("ab", 256), ""
q

q = grille("abcdef", 5), "df"
q
q = grille("abcde", 32), ""
q
q = grille("tcddoadepwweasresd", 77098), "codewars"
q
