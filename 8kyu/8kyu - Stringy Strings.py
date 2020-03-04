# 8kyu - Stringy Strings

""" write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.

the string should start with a 1.

a string with size 6 should return :'101010'.
with size 4 should return : '1010'.
with size 12 should return : '101010101010'.

The size will always be positive and will only use whole numbers.  """


# def stringy(size):
#     return ('10' * size)[0:size]

# def stringy(size):
#     return ('10' * size)[:size]

def stringy(size):
    return '10' * (size // 2) + '1' * (size % 2)


q = stringy(10)[0]  # '1'
q
q = stringy(3)  # '101'
q
q = stringy(5)  # '10101'
q
q = stringy(12)  # '101010101010'
q
q = stringy(26)  # '10101010101010101010101010'
q
q = stringy(28)  # '1010101010101010101010101010'
q
