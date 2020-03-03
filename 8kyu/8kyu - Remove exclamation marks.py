# 8kyu - Remove exclamation marks

""" Write function RemoveExclamationMarks which removes all exclamation marks from a given string. """


def remove_exclamation_marks(s):
    return s.replace('!', '')


q = remove_exclamation_marks("Hello World!")  # "Hello World"
q
q = remove_exclamation_marks("Hello World!!!")  # "Hello World"
q
q = remove_exclamation_marks("Hi! Hello!")  # "Hi Hello"
q
q = remove_exclamation_marks("")  # ""
q
q = remove_exclamation_marks("Oh, no!!!")  # "Oh, no"
q
