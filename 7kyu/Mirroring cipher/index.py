""" 7kyu - Mirroring cipher

You're back at your newly acquired decrypting job for the secret organization when a new assignment comes in. 
Apparently the enemy has been communicating using a device they call "The Mirror".
It is a rudimentary device with encrypts the message by switching its letter with its mirror opposite 
(A => Z), (B => Y), (C => X) etc.

Your job is to build a method called "mirror" which will decrypt the messages. Resulting messages will be in lowercase.

To add more secrecy, you are to accept a second optional parameter, telling you which letters or characters 
are to be reversed; if it is not given, consider the whole alphabet as a default.

To make it a bit more clear: e.g. in case of "abcdefgh" as the second optional parameter, 
you replace "a" with "h", "b" with "g" etc. .

For example:

mirror("Welcome home"), "dvoxlnv slnv" //whole alphabet mirrored here
mirror("hello", "abcdefgh"), "adllo" //notice only "h" and "e" get reversed """

from string import ascii_lowercase as abc

# def mirror(code, option=abc):
#     if option is abc:
#         return code.lower().translate(str.maketrans(abc, abc[::-1]))
#     else:
#         return code.lower().translate(str.maketrans(option, option[::-1]))

def mirror(code, key=abc):
    return code.lower().translate(str.maketrans(key, key[::-1]))


# No optional parameter given, reverse whole alphabet
q = mirror("Welcome home"), "dvoxlnv slnv"
q
q = mirror("hello"), "svool"
q
q = mirror("goodbye"), "tllwybv"
q
q = mirror("ngmlsoor"), "mtnohlli"
q
q = mirror("gsrh rh z hvxivg"), "this is a secret"
q

# Second parameter given
q = mirror("Welcome home", "w"), "welcome home"
q
q = mirror("hello", "abcdefgh"), "adllo"
q
q = mirror("goodbye", ""), "goodbye"
q
q = mirror("CodeWars", "+-*/="), "codewars"
q
q = mirror("this is a secret", " *"), "this*is*a*secret"
q
