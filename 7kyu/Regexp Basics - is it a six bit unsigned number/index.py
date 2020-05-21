# 7kyu - Regexp Basics - is it a six bit unsigned number?

"""Implement six_bit_number, which should return true if given object is a number 
representable by 6 bit unsigned integer (0-63), false otherwise.

It should only accept numbers in canonical representation, so no leading +, extra 0s, spaces etc.

Fundamentals | Regular Expressions | Declarative Programming | Advanced Language Features | Strings """


# def six_bit_number(n):
#     return n in map(str, range(64))

import re

# def six_bit_number(n):
#     return re.findall('[1-6][0-3]|[1-5]\d|\d', n) == [n]

# def six_bit_number(n):
#     return re.findall('[1-6][0-3]|[1-5]?\d', n) == [n]

def six_bit_number(n):
    return re.findall('6[0-3]|[1-5]?\d', n) == [n]


q = six_bit_number("")  # False
q
q = six_bit_number("0")  # True
q
q = six_bit_number("00")  # False
q
q = six_bit_number("55")  # True
q
q = six_bit_number("63")  # True
q
q = six_bit_number("64")  # False
q
q = six_bit_number("-0")  # False
q
q = six_bit_number("-5")  # False
q
q = six_bit_number("05")  # False
q
q = six_bit_number("5")  # True
q
