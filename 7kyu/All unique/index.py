# 7kyu - All unique

""" Write a program to determine if a string contains all unique characters. 
Return true if it does and false otherwise.

The string may contain any of the 128 ASCII characters. """


def has_unique_chars(string):
    return len(string) <= 128 and len(string) == len(set(string))


q = has_unique_chars("abcdef"), True
q
q = has_unique_chars("++-"), False
q
q = has_unique_chars("  nAa"), False
q
