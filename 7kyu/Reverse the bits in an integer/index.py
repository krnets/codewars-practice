""" 7kyu - Reverse the bits in an integer

Write a function that reverses the bits in an integer.

For example, the number 417 is 110100001 in binary. Reversing the binary is 100001011 which is 267.

You can assume that the number is not negative. """


def reverse_bits(n):
    return int(bin(n)[:1:-1], 2)


q = reverse_bits(417), 267
q
q = reverse_bits(267), 417
q
q = reverse_bits(0), 0
q
q = reverse_bits(2017), 1087
q
q = reverse_bits(1023), 1023
q
q = reverse_bits(1024), 1
q
