# 8kyu - Vowel remover

""" Create a function called shortcut to remove all the lowercase vowels in a given string.

shortcut("codewars") # --> cdwrs
shortcut("goodbye")  # --> gdby

Don't worry about uppercase vowels. """


def shortcut(s):
    return ''.join(c for c in s if c not in 'aeiou')


q = shortcut('hello')  # 'hll'
q
