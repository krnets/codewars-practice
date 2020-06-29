""" 6kyu - ROT13 variant cipher

You have been recruited by an unknown organization for your cipher encrypting/decrypting skills.
Being new to the organization they decide to test your skills.
Your first test is to write an algorithm that encrypts the given string in the following steps.

    The first step of the encryption is a standard ROT13 cipher. 
    This is a special case of the caesar cipher where the letter is encrypted with its key 
    that is thirteen letters down the alphabet,
    i.e. A => N, B => O, C => P, etc..

    Part two of the encryption is to take the ROT13 output and replace each letter with its exact opposite. 
    A => Z, B => Y, C => X. The return value of this should be the encrypted message.

Do not worry about capitalization or punctuation. All encrypted messages should be lower case and punctuation free.
As an example, the string "welcome to our organization" should return "qibkyai ty ysv yvgmzenmteyz".  """

from string import ascii_lowercase as abc

# def encrypter(strng):
#     strng = strng.translate(str.maketrans(abc, abc[13:]+abc[:13]))
#     strng = strng.translate(str.maketrans(abc, abc[::-1]))
#     return strng

# def encrypter(strng):
#     return strng.translate(str.maketrans(abc, abc[12::-1]+abc[:12:-1]))

def encrypter(strng):
    return strng.translate(str.maketrans(abc[::-1], abc[13:]+abc[:13]))

q = encrypter("amz"), "man"
q
q = encrypter("welcome to the organization"), "qibkyai ty tfi yvgmzenmteyz"
q
q = encrypter("hello"), "fibby"
q
q = encrypter("my name is"), "ao zmai eu"
q
q = encrypter("goodbye"), "gyyjloi"
q
