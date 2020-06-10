""" 6kyu - Remember

Write a function that takes a string and returns an array of the repeated characters (letters, numbers, whitespace) in the string.
If a charater is repeated more than once, only show it once in the dups array.
Characters should be shown by the order of their first repetition. 
Note that this may be different from the order of first appearance of the character.
Characters are case sensitive. """


def remember(st):
    seen = []
    dups = []
    for c in st:
        if c in seen and c not in dups:
            dups.append(c)
        else:
            seen.append(c)
    return dups


q = remember('apple'), ["p"]
q
q = remember("apPle"), []
q
q = remember("pippi"), ["p", "i"]
q
q = remember('Pippi'), ["p", "i"]
q
q = remember("limbojackassin the garden"), ["a", "s", "i", " ", "e", "n"]
q
q = remember("11pinguin"), ["1", "i", "n"]
q
