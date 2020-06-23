""" 6kyu - Simple Fun #141: Hamming Distance

 The hamming distance between a pair of numbers is the number of binary bits that differ in their binary notation.

For a = 25, b= 87, the result should be 4

25: 00011001
87: 01010111

The hamming distance between these two would be 4 ( the 2nd, 5th, 6th, 7th bit ).

    [input] integer a
    First Number. 1 <= a <= 2^20

    [input] integer b
    Second Number. 1 <= b <= 2^20

    [output] an integer
    Hamming Distance """


# def hamming_distance(a, b):
#     a, b = bin(a)[2:].zfill(32), bin(b)[2:].zfill(32)
#     return sum(map(str.__ne__, a, b))

def hamming_distance(a, b):
    a, b = map(lambda x: bin(x)[2:].zfill(32), (a, b))
    return sum(map(str.__ne__, a, b))

# def hamming_distance(a, b):
#     return bin(a ^ b).count('1')


q = hamming_distance(25, 87), 4
q
q = hamming_distance(256, 302), 4
q
q = hamming_distance(543, 634), 4
q
q = hamming_distance(34013, 702), 7
q
q = hamming_distance(510224,  47712), 11
q
