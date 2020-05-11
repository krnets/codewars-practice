# Beta - Find GCF (Greatest Common Factor)

""" Create a simple algorithm to find the Greatest Comon Factor (GCF) between two number. 
Your function should accept two integers and should return an integer as GCF between inputs.

For example:

largest_factor(50,25)
should return 25

This was because 50 and 25 are both divisible by 25 which is the possible largest factor between the two.

largest_factor(81,63)
should return 9

largest_factor(24,54)
should return 6

largest_factor(67,19)
should return 1

Acceptable return value is greater or equal to 1, also, num1 and num2 should be an integer greater than 0. """


# def gcd(a, b):
#     return a if b == 0 else gcd(b, a % b)

# def largest_factor(num1, num2):
#     return gcd(num1, num2)

from fractions import gcd as largest_factor

q = largest_factor(50, 25), 25, "GCF for 50 and 25 is 25"
q
q = largest_factor(81, 63), 9, "GCF for 81 and 63 is 9"
q
q = largest_factor(24, 54), 6, "GCF for 54 and 24 is 6"
q
q = largest_factor(67, 19), 1, "Both are prime, their GCF is 1"
q
