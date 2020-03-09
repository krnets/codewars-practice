# 7kyu - Testing 1-2-3

""" Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
Write a function which takes a list of strings and returns each line prepended by the correct number.
The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples:

number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"] """

# from itertools import count

# def number(lines):
#     counter = count(1)
#     return [str(next(counter)) + ': ' + x for x in lines]

def number(lines):
    return [f'{i + 1}: {x}' for (i, x) in enumerate(lines)]

# def number(lines):
#     return ['{}: {}'.format(i, x) for(i, x) in enumerate(lines, 1)]



q = number([])  # []
q
q = number(["a", "b", "c"])  # ["1: a", "2: b", "3: c"]
q
