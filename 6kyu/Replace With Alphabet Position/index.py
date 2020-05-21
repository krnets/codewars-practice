# 6kyu - Replace With Alphabet Position

""" Given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

alphabet_position("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string) """

# import re

# def alphabet_position(text):
#     return ' '.join(str(ord(x) - 96) for x in re.sub(r"\W", '', text.lower()))

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

q = alphabet_position("The sunset sets at twelve o' clock.")
q
#  "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

q = alphabet_position("The narwhal bacons at midnight.")
q
#  "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
