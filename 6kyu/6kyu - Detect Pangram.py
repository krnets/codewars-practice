# 6kyu - Detect Pangram

""" A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. 
Return True if it is, False if not. Ignore numbers and punctuation. """

from string import ascii_lowercase as abc

# def is_pangram(s):
#     return len(set(c for c in s.lower() if c in abc)) == len(abc)


# def is_pangram(s):
#     s = s.lower()
#     return all(c in s for c in abc)

# def is_pangram(s):
#     return set(s.lower()).issuperset(set(abc))

def is_pangram(s):
    return set(abc).issubset(set(s.lower()))


pangram = "The quick, brown fox jumps over the lazy dog!"
q = is_pangram(pangram)  # True
q
q = is_pangram("This isn't a pangram!")  # False
q
q = is_pangram("abcdefghijklmopqrstuvwxyz")  # False
q
