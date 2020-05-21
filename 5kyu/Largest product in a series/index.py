# 5kyu - Largest product in a series

""" Complete the greatestProduct method so that it'll find the greatest product of 
five consecutive digits in the given string of digits.

For example:

greatestProduct("123834539327238239583") // should return 3240

The input string always has more than five digits.

Adapted from Project Euler. """


from operator import mul
from functools import reduce

# def greatest_product(n):
#     return max(reduce(mul, map(int, list(n[i-4:i+1]))) for i in range(4, len(n)))

# def greatest_product(n):
#     return max(reduce(mul, map(int, list(n[i-5:i]))) for i in range(5, len(n)+1))

def greatest_product(n):
    return max(reduce(mul, map(int, list(n[i:i+5]))) for i in range(len(n)-4))


q = greatest_product("123834539327238239583"), 3240
q
q = greatest_product("395831238345393272382"), 3240
q
q = greatest_product("92494737828244222221111111532909999"), 5292
q
q = greatest_product("92494737828244222221111111532909999"), 5292
q
q = greatest_product("02494037820244202221011110532909999"), 0
q
