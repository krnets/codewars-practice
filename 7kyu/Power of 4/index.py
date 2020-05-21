# 7kyu - Power of 4

""" Write a method that returns true if a given parameter is a power of 4, and false if it's not. 
If parameter is not an Integer (eg String, Array) method should return false as well.

isPowerOf4 1024 #should return True
isPowerOf4  102 #should return False
isPowerOf4   64 #should return True """

import math

# def powerof4(n):
#     return type(n) == int and n > 0 and math.log(n, 4).is_integer()

def powerof4(n):
    return type(n) is int and n > 0 and math.log(n, 4).is_integer()


q = powerof4(4), True
q
q = powerof4(40), False
q
q = powerof4(1), True
q
