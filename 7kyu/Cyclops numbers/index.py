# 7kyu - Cyclops numbers

""" A cyclops number is a number in binary that is made up of all 1's, with one 0 in the exact middle. 
That means all cyclops numbers must have an odd number of digits for there to be an exact middle.

A couple examples:

101
11111111011111111

You must take an input, n, that will be in decimal format (base 10), then return True if that number 
will be a cyclops number when converted to binary, or False if it won't.

Assume n will be a positive integer.

5 in biinary 0b101 because 101 is made up of all "1"s with a "0" in the middle, 101 is a cyclops number. return True

13 in binary 0b1101 because 1101 has an even number of bits, it cannot be a cyclops. return False

17 in binary 0b10001 because 10001 has more than 1 "0" it cannot be a cyclops number. return False """


# def cyclops(n):
#     sbin = bin(n)[2:]
#     half = len(sbin) // 2
#     midp = sbin[half]
#     without_middle = '0' not in sbin[0:len(sbin) // 2] + sbin[half + 1:]
#     return False if len(sbin) % 2 == 0 or len(sbin) < 3 or midp != '0' else without_middle

# def cyclops(n):
#     binary = bin(n)[2:]
#     return binary[::-1] == binary and binary.count('0') == 1

def cyclops(n):
    binary = bin(n)[2:]
    return binary.count('0') == 1 and binary[::-1] == binary


q = cyclops(1)  # False
q
q = cyclops(5)  # True
q
q = cyclops(3)  # False
q
q = cyclops(13)  # False
q
q = cyclops(27)  # True
q
q = cyclops(17)  # False
q
