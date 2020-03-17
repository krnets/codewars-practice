# 7kyu - Count the Characters

""" The goal of this kata is to write a function that takes two inputs: a string and a character. 
The function will count the number of times that character appears in the string. The count is case insensitive.

For example:

count_char("fizzbuzz","z") => 4
count_char("Fancy fifth fly aloof","f") => 5

The character can be any alphanumeric character.  """

# from collections import Counter

# def count_char(str, ch):
#     return Counter(str.lower())[ch.lower()]

def count_char(str, ch):
    return str.lower().count(ch.lower())


q = count_char("Hello there", "e")  # 3
q
q = count_char("Hello there", "t")  # 1
q
q = count_char("Hello there", "h")  # 2
q
q = count_char("Hello there", "L")  # 2
q
q = count_char("Hello there", " ")  # 1
q
