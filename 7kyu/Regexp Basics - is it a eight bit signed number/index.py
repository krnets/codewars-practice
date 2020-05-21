# 7kyu - Regexp Basics - is it a eight bit signed number?

""" Implement eight_bit_signed_number() which should return True if given object is a number 
representable by 8 bit signed integer (-128 to -1 or 0 to 127), False otherwise.

It should only accept numbers in canonical representation, so no leading +, extra 0s, spaces etc. """

import re

# def signed_eight_bit_number(number):
#     return number in map(str, range(-128, 128))

# def signed_eight_bit_number(number):
#     return re.findall('-1[1-2][0-8]|1[1-2][0-7]|-1\d\d|1\d\d|-[1-9]\d|[1-9]\d|-[1-9]|\d', number) == [number]

# def signed_eight_bit_number(number):
#     return bool(re.fullmatch('^(-(1(2[0-8]|[01][0-9])|[1-9][0-9]?)|(1(2[0-7]|[01][0-9])|[1-9]?[0-9]))$', number))

# def signed_eight_bit_number(number):
#     return bool(re.match("(0|-128|-?([1-9]|[1-9]\d|1[01]\d|12[0-7]))\Z", number))

def signed_eight_bit_number(number):
    return bool(re.match('(0|-128|-?(12[0-7]|1[01]\d|[1-9]\d|[1-9]))\Z', number))

# SIGNED_BYTE_PATTERN = re.compile(r'''
#     \A
#     (?:
#         0 |
#         -? (?:
#             1 (?:
#                 [01] \d? |
#                 2 [0-7]? |
#                 [3-9] )? |
#             [2-9] \d? ) |
#         -128 )
#     \Z
# ''', re.VERBOSE)


# SIGNED_BYTE_PATTERN = re.compile('''
#     \A
#     (0 | -128 | -? (1 ([01] \d | 2 [0-7] | [3-9] ) | [2-9] \d ))
#     \Z
# ''', re.VERBOSE)

# SIGNED_BYTE_PATTERN = re.compile('\A(?:0 |-? (?:1 (?:[01] \d? |2 [0-7]? |[3-9] )? | [2-9] \d? ) |-128 )\Z', re.X)


# def signed_eight_bit_number(number):
#     return bool(SIGNED_BYTE_PATTERN.search(number))


q = signed_eight_bit_number(""), False
q
q = signed_eight_bit_number("0"), True
q
q = signed_eight_bit_number("00"), False
q
q = signed_eight_bit_number("-0"), False
q
q = signed_eight_bit_number("55"), True
q
q = signed_eight_bit_number("-23"), True
q
q = signed_eight_bit_number("042"), False
q
q = signed_eight_bit_number("-127"), True
q
q = signed_eight_bit_number("127"), True
q
q = signed_eight_bit_number("128"), False
q
q = signed_eight_bit_number("999"), False
q
q = signed_eight_bit_number("-128"), True
q
q = signed_eight_bit_number("-129"), False
q
q = signed_eight_bit_number("-999"), False
q
q = signed_eight_bit_number("1\n"), False
q
q = signed_eight_bit_number("1 "), False
q
q = signed_eight_bit_number(" 1"), False
q
q = signed_eight_bit_number("1\n2"), False
q
q = signed_eight_bit_number("+1"), False
q
q = signed_eight_bit_number("--1"), False
q
q = signed_eight_bit_number("1\n"), False
q
q = signed_eight_bit_number("1 "), False
q
q = signed_eight_bit_number(" 1"), False
q
q = signed_eight_bit_number("1\n2"), False
q
q = signed_eight_bit_number("+1"), False
q
q = signed_eight_bit_number("--1"), False
q
