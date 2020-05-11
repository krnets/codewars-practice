# 7kyu - Greatest Common Divisor Bitcount

""" The objective is to write a method that takes two integer parameters and returns a single integer 
equal to the number of 1s in the binary representation of the greatest common divisor of the parameters.

Taken from Wikipedia: "In mathematics, the greatest common divisor (gcd) of two or more integers, 
when at least one of them is not zero, is the largest positive integer that divides the numbers 
without a remainder. For example, the GCD of 8 and 12 is 4."

For example: the greatest common divisor of 300 and 45 is 15. The binary representation of 15 is 1111, 
so the correct output would be 4.

If both parameters are 0, the method should return 0. The function must be able to handle negative input. """


# def binary_gcd(x, y):
#         return gcd(b, a % b) if b > 0 else a
#     return 1 if x < 0 or y < 0 else bin(gcd(x, y)).count('1')

# def gcd(a, b):
#     return abs(a) if b == 0 else gcd(b, a % b)

from fractions import gcd

def binary_gcd(x, y):
    return bin(gcd(x, y)).count('1')


q = binary_gcd(666666, 333111), 6
q
q = binary_gcd(545034, 5), 1
q
q = binary_gcd(0, 0), 0
q
q = binary_gcd(0, 76899299), 14
q
q = binary_gcd(666666, 333111), 6
q
q = binary_gcd(-124, -16), 1
q
