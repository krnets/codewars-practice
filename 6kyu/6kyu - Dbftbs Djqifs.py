# 6kyu - Dbftbs Djqifs

""" Caesar Ciphers are one of the most basic forms of encryption. 
It consists of a message and a key, and it shifts the letters of the message for the value of the key.

Read more about it here: https://en.wikipedia.org/wiki/Caesar_cipher
Your task

Your task is to create a function encryptor that takes 2 arguments - key and message - and returns the encrypted message.

Make sure to only shift letters, and be sure to keep the cases of the letters the same. 
All punctuation, numbers, spaces, and so on should remain the same.

Also be aware of keys greater than 26 and less than -26. There's only 26 letters in the alphabet!
Examples

A message 'Caesar Cipher' and a key of 1 returns 'Dbftbs Djqifs'.
A message 'Caesar Cipher' and a key of -1 returns 'Bzdrzq Bhogdq'. """

# def encryptor(key, message):
#     res = ''
#     for x in message:
#         if x.isupper():
#             res += chr(((ord(x) - 65 + key) % 26) + 65)
#         elif x.islower():
#             res += chr(((ord(x) - 97 + key) % 26) + 97)
#         else:
#             res += x
#     return res


def encryptor(key, message):
    res = ''
    for x in message:
        if x.isalpha():
            base = ord('A') if x.isupper() else ord('a')
            res += chr(base + (ord(x) + key - base) % 26)
        else:
            res += x
    return res


q = encryptor(13, '')  # ''
q
q = encryptor(13, 'Caesar Cipher')  # 'Pnrfne Pvcure'
q
q = encryptor(-5, 'Hello World!')  # 'Czggj Rjmgy!'
q
q = encryptor(27, 'Whoopi Goldberg')  # 'Xippqj Hpmecfsh'
q
