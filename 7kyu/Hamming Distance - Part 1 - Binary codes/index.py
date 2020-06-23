""" 7kyu - Hamming Distance - Part 1: Binary codes

The hamming distance of two equal-length strings is the number of positions, in which the two string differ. 
In other words, the number of character substitutions required to transform one string into the other.

For this first Kata, you will write a function hamming_distance(a, b) with two equal-length strings 
containing only 0s and 1s as parameters. There is no need to test the parameters for validity (but you can, 
if you want).The function's output should be the hamming distance of the two strings as an integer.

hamming_distance('100101', '101001') == 2
hamming_distance('1010', '0101') == 4 """


# def hamming_distance(a, b):
#     return sum(1 for x, y in zip(a, b) if int(x) - int(y) != 0)

# def hamming_distance(a, b):
#     return sum(x != y for x, y in zip(a, b))

from operator import ne

def hamming_distance(a, b):
    return sum(map(ne, a, b))


q = hamming_distance('100101', '101001'), 2
q
q = hamming_distance('1010', '0101'), 4
q
q = hamming_distance('100101011011010010010', '101100010110010110101'), 9
q
