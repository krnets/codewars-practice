""" 7kyu - Binary operations #1

Your work is to write a method that takes a value and an index, and returns the value with the bit at given index flipped.
The bits are numbered from the least significant bit (index 1).

Example:

flip_bit(15, 4) == 7 # 15 in binary is 1111, after flipping 4th bit, it becomes 0111, i.e. 7
flip_bit(15, 5) == 31 # 15 in binary is 1111, 5th bit is 0, after flipping, it becomes 11111, i.e., 31

Note : index number can be out of number's range : e.g number is 3 (it has 2 arr_bits) and index number is 8 -> result will be 131  """

import sys


# def flip_bit(value, bit_index):
#     arr_bits = [x for x in bin(value)[2:].rjust(64, '0')]
#     arr_bits[-bit_index] = str(abs(int(arr_bits[-bit_index])-1))
#     return int(''.join(arr_bits), 2)

# def flip_bit(value, bit_index):
#     arr_bits = [x for x in bin(value)[2:].zfill(64)]
#     arr_bits[-bit_index] = str(abs(int(arr_bits[-bit_index])-1))
#     return int(''.join(arr_bits), 2)

def flip_bit(value, bit_index):
    return value ^ (1 << bit_index-1)


q = flip_bit(0, 16), 1 << 15
q
q = flip_bit(sys.maxsize - 1, 1), sys.maxsize
q
q = flip_bit((1 << 31) - 1, 31), (1 << 30) - 1
q
q = flip_bit(127, 8), 0xFF
q
