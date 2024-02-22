import re


# def Hangman(guess, word):
#     pattern = "[^" + guess.lower() + "]"
#     return re.sub(pattern, "_", word.lower())


def Hangman(guess, word):
    return "".join(("_", c)[c == guess.lower()] for c in word.lower())
