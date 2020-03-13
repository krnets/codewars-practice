# 7kyu - Character Counter

""" You are going to be given a word. 
Your job will be to make sure that each character in that word has the exact same number of occurrences. 
You will return true if it is valid, or false if it is not.

"abcabc" is a valid word because 'a' appears twice, 'b' appears twice, and'c' appears twice.
"abcabcd" is NOT a valid word because 'a' appears twice, 'b' appears twice, 'c' appears twice, 
but 'd' only appears once! "123abc!" is a valid word because all of the characters only appear once in the word.

For this kata, capitals are considered the same as lowercase letters. Therefore: 'A' == 'a' .

Input
A string (no spaces) containing [a-z],[A-Z],[0-9] and common symbols. The length will be 0 < string < 100.

Output
true if the word is a valid word, or false if the word is not valid. """

from collections import Counter

# def validate_word(word):
#     vals = list(Counter(word.lower()).values())
#     return list(filter(lambda x: x == vals[0], vals)) == vals

def validate_word(word):
    return len(set(Counter(word.lower()).values())) == 1


q = validate_word("abcabc")  # True
q
q = validate_word("Abcabc")  # True
q
q = validate_word("AbcabcC")  # False
q
q = validate_word("AbcCBa")  # True
q
q = validate_word("pippi")  # False
q
q = validate_word("?!?!?!")  # True
q
q = validate_word("abc123")  # True
q
q = validate_word("abcabcd")  # False
q
q = validate_word("abc!abc!")  # True
q
q = validate_word("abc:abc")  # False
q
