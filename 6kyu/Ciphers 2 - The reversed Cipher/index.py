""" 6kyu - Ciphers #2 - The reversed Cipher

This is a lame method I use to write things such that my friends don't understand. 
It's still fairly readable if you think about it.

How this cipher works

First, you need to reverse the string. Then, the last character in the original string 
(the first character in the reversed string) needs to be moved to the back. 
Words will be separated by spaces, and punctuation marks can be counted as part of the word.

encode("Hello World!"); // => "lleHo dlroW!"

This is because "Hello" reversed is "olleH" and "o" is moved to the back, and so on. 
The exclamation mark is considered to be part of the word "World". """


# def encode(s):
#     return ' '.join(word[::-1][1:]+word[::-1][0] for word in s.split())

def encode(s):
    return ' '.join(word[::-1][1:]+word[-1] for word in s.split())


q = encode("Hello World!"), "lleHo dlroW!"
q
