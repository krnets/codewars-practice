# 7kyu - Convert Integer to Binary

""" Convert integers to binary as simple as that. 
You would be given an integer as a argument and you have to return its binary form. 
To get an idea about how to convert a decimal number into a binary number, visit here.

Notes: negative numbers should be handled as two's complement; assume all numbers are 
integers stored using 4 bytes (or 32 bits) in any language.

Your output should ignore leading 0s.

to_binary(3)=="11"
to_binary(-3)=="11111111111111111111111111111101" """


# def to_binary(n):
#     return f'{n & 0xffffffff:b}'

# def to_binary(n):
#     return bin(n & (2**32-1))[2:]

# def to_binary(n):
#     return '{:b}'.format(n & 0xffffffff)

def to_binary(n):
    return format(n & 0xffffffff, 'b')


q = to_binary(2), "10"
q
q = to_binary(3), "11"
q
q = to_binary(4), "100"
q
q = to_binary(-3), "11111111111111111111111111111101"
q
q = to_binary(0), "0"
q
