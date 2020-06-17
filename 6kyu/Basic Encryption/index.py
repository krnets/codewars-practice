""" 6kyu - Basic Encryption

The most basic encryption method is to map a char to another char by a certain math rule. 
Because every char has an ASCII value, we can manipulate this value with a simple math expression. 
For example 'a' + 1 would give us 'b', because 'a' value is 97 and 'b' value is 98.

You will need to write a method which does exactly that -

get a string as text and an int as the rule of manipulation, and should return encrypted text.

encrypt("a",1) = "b"

Full ascii table is used on our question (256 chars) - so 0-255 are the valid values. """


# def encrypt(text, rule):
#     return ''.join(chr((ord(c) + rule) % 256) for c in text)

def encrypt(text, rule):
    return ''.join(chr((ord(c) + rule) & 255) for c in text)


q = encrypt("", 1), ""
q
q = encrypt("a", 1), "b"
q
q = encrypt("please encrypt me", 2), "rngcug\"gpet{rv\"og"
q
