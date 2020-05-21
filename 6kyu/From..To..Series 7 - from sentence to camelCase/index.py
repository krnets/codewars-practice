# 6kyu - From..To..Series #7: from sentence to camelCase. Can you convert it?

""" Give you a sentence s. It contains some words and separated by spaces. 
Another arguments is n, its a number(1,2 or 3). You should convert s to camelCase n.

There are three kinds of camelCase:

 camelCase 1: The first letter of each word should be capitalized. 
               Except for the first word.

 Example: "Hello world"  -->  "helloWorld"

 camelCase 2: The last letter of each word should be capitalized. 
               Except for the last word. 

 Example: "Hello world"  -->  "hellOworld"

 camelCase 3: The first and last letters of each word should be capitalized. 
               Except for the first and lasts letter of sentence. 

 Example: "Hello world"  -->  "hellOWorld" 

You can assume that all of the input data is valid. That is: s always be a string; 
It contains at least two words; Each word contains only letters(a-zA-Z); 
Each word contains ar least three letters; n always be 1,2 or 3. """

# def toCamelCase(s, n):
#     if n == 1:
#         return s[:1].lower() + s.title().replace(' ', '')[1:]
#     elif n == 2:
#         return ''.join(word[::-1].title()[::-1] for word in s.lower().split())[:-1] + s[-1].lower()
#     elif n == 3:
#         words = [word.title() for word in s.lower().split()]
#         words = [x[:-1] + x[-1].capitalize() for x in words]
#         return s[0].lower() + ''.join(words)[1:-1] + s[-1].lower()

import re

# def toCamelCase(s, n):
#     return re.sub([r' \w', r'\w ', r' \w|\w(?= )'][n-1], lambda m: m.group().upper().strip(), s.lower())

def toCamelCase(s, n):
    return re.sub([r'\s\w', r'\w\s', r'\s\w|\w(?=\s)'][n-1], lambda m: m.group().upper().strip(), s.lower())


q = toCamelCase("hello world", 1), "helloWorld"
q
q = toCamelCase("Hello world", 1), "helloWorld"
q
q = toCamelCase("Each number plus one", 1), "eachNumberPlusOne"
q

q = toCamelCase("hello world", 2), "hellOworld"
q
q = toCamelCase("Each number plus one", 2), "eacHnumbeRpluSone"
q


q = toCamelCase("hello world", 3), "hellOWorld"
q
q = toCamelCase("Each number plus one", 3), "eacHNumbeRPluSOne"
q
