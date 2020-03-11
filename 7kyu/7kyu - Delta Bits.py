# 7kyu - Delta Bits

""" Complete the function to determine the number of bits required to convert integer A to integer B (where A and B >= 0)

The upper limit for A and B is 216, int.MaxValue or similar.

For example, you can change 31 to 14 by flipping the 4th and 0th bit:

 31  0 0 0 1 1 1 1 1
 14  0 0 0 0 1 1 1 0
---  ---------------
bit  7 6 5 4 3 2 1 0

Thus 31 and 14 should return 2. """


# def convert_bits(a, b):
#     if b > a:
#         a, b = b, a
#     aa = bin(a)[2:]
#     bb = bin(b)[2:].zfill(len(bin(a)[2:]))
#     return sum(1 for i in range(len(aa)) if aa[i] != bb[i])

def convert_bits(a, b):
    return bin(a ^ b).count('1')


q = convert_bits(31, 14)  # 2
q
q = convert_bits(7, 17)  # 3
q
q = convert_bits(31, 0)  # 5
q
q = convert_bits(0, 0)  # 0
q
