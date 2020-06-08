""" 7kyu - Find the Middle of the Product

Given a string of characters, I want the function find_middle() to return the middle number 
in the product of each digit in the string.

Example: 's7d8jd9' -> 7, 8, 9 -> 7*8*9=504, thus 0 should be returned as an integer.

Not all strings will contain digits. In this case and the case for any non-strings, return -1.

If the product has an even number of digits, return the middle two digits

Example: 1563 -> 56

NOTE: Remove leading zeros if product is even and the first digit of the two is a zero. Example 2016 -> 1 """


from functools import reduce
from operator import mul
import re

# def find_middle(string):
#     if not isinstance(string, str) or not bool(re.findall(r'\d', string)):
#         return -1
#     digits = [int(x) for x in string if x.isdigit()]
#     product = str(reduce(mul, digits, 1))
#     half = len(product) // 2
#     return int(product[half]) if len(product) % 2 else int(product[half-1:half+1])


# def find_middle(string):
#     if not isinstance(string, str) or not bool(re.findall(r'\d', string)):
#         return -1
#     digits = [int(x) for x in string if x.isdigit()]
#     product = str(reduce(mul, digits, 1))
#     half = (len(product)-1) // 2
#     return int(product[half:-half or len(product)])

def find_middle(string):
    if not isinstance(string, str) or not bool(re.findall(r'\d', string)):
        return -1
    digits = [int(x) for x in string if x.isdigit()]
    product = str(reduce(mul, digits, 1))
    middle = (len(product)-1) // 2
    return int(product[middle:-middle or len(product)])


q = find_middle('s7d8jd9'), 0
q
q = find_middle('58jd9fgh/fgh6s.,sdf'), 16
q
q = find_middle(None), -1
q
q = find_middle([1, 2, 3]), -1
q
