# 6kyu - WeIrD StRiNg CaSe

""" Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string 
with all even indexed characters in each word upper cased, and all odd indexed characters in each word 
lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that 
character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). 
Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').


to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe' """

# def to_weird_case(string):
#     words = string.split()
#     res = []
#     for word in words:
#         res.append(''.join(x.lower() if i % 2 else x.upper()
#                            for i, x in enumerate(word)))
#     return ' '.join(res)


# def to_weird_case(string):
#     res = []
#     for word in string.split():
#         res.append(''.join(x.lower() if i % 2 else x.upper() for i, x in enumerate(word)))
#     return ' '.join(res)


def to_weird_case(string):
    return ' '.join(''.join(x.lower() if i % 2 else x.upper() for i, x in enumerate(word)) for word in string.split())


# should return the correct value for a single word
q = to_weird_case('This'), 'ThIs'
q
q = to_weird_case('is'), 'Is'
q

# should return the correct value for multiple words
q = to_weird_case('This is a test'), 'ThIs Is A TeSt'
q
