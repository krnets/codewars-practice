# 7kyu - Word to binary

""" Write a function that takes a string and returns an array containing 
binary numbers equivalent to the ASCII codes of the characters of the string. 
The binary strings should be eight digits long.

Example: 'man' should return [ '01101101', '01100001', '01101110' ] """


# def word_to_bin(word):
#     return [bin(ord(x)).replace('b', '') for x in word]

# def word_to_bin(word):
#     return ['{:08b}'.format(ord(x)) for x in word]

# def word_to_bin(word):
#     return [f'{ord(x):08b}' for x in word]

def word_to_bin(word):
    return [format(ord(x), '08b') for x in word]


q = word_to_bin('man')
q
#      [ '01101101', '01100001', '01101110' ]
q = word_to_bin('AB')
q
#      ['01000001', '01000010']
q = word_to_bin('wecking')
q
#      [ '01110111', '01100101', '01100011', '01101011', '01101001', '01101110', '01100111' ]
q = word_to_bin('Ruby')
q
# [ '01010010', '01110101', '01100010', '01111001' ]
q = word_to_bin('Yosemite')
q
#      [ '01011001', '01101111', '01110011', '01100101', '01101101', '01101001', '01110100', '01100101' ]
