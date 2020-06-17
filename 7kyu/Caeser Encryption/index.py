""" 7kyu - Caeser Encryption

You have invented a time-machine which has taken you back to ancient Rome. 
Caeser is impressed with your programming skills and has appointed you to be the new information security officer.

Caeser has ordered you to write a Caeser cipher to prevent Asterix and Obelix from reading his emails.

A Caeser cipher shifts the letters in a message by the value dictated by the encryption key. 
Since Caeser's emails are very important, he wants all encryptions to have upper-case output, for example:

If key = 3 "hello" -> KHOOR If key = 7 "hello" -> OLSSV

Input will consist of the message to be encrypted and the encryption key. """

from string import ascii_lowercase as abc, ascii_uppercase as ABC

# def caeser(message, key):
#     return message.translate(str.maketrans(abc, (abc+abc)[key:][:len(abc)])).upper()


def caeser(message, key):
    return message.translate(str.maketrans(abc, ABC[key:] + ABC[:key]))


q = caeser("hello world", 0), "HELLO WORLD"
q
q = caeser("hello", 7), "OLSSV"
q
