# 7kyu - Regexp Basics - is it a eight bit unsigned number?

""" Implement eight_bit_number, which should return true if given object is a number 
representable by 8 bit unsigned integer (0-255), false otherwise.

It should only accept numbers in canonical representation, so no leading +, extra 0s, spaces etc.

Fundamentals | Regular Expressions | Declarative Programming | Advanced Language Features | Strings """

# def eight_bit_number(n):
#     if n.isdigit():
#         if int(n[0]) == 0 and int(len(n)) > 1:
#             return False
#         elif int(n) < 0 or int(n) >= 256:
#             return False
#         else:
#             return True
#     else:
#         return False

# def eight_bit_number(n):
#     return n in map(str, range(256))

import re

# def eight_bit_number(n):
#     return re.findall('25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d', n) == [n] and len(n) > 0

# def eight_bit_number(n):
#     return bool(re.fullmatch(r"([1-9]?|1\d|2[0-4])\d|25[0-5]", n))

def eight_bit_number(n):
    return re.findall('25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d', n) == [n]

# def eight_bit_number(n):
#     return [n] == re.findall('25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d', n)


q = eight_bit_number("")  # False
q
q = eight_bit_number("0")  # True
q
q = eight_bit_number("00")  # False
q
q = eight_bit_number("55")  # True
q
q = eight_bit_number("042")  # False
q
q = eight_bit_number("123")  # True
q
q = eight_bit_number("255")  # True
q
q = eight_bit_number("256")  # False
q
q = eight_bit_number("999")  # False
q
q = eight_bit_number("-1")  # False
q
