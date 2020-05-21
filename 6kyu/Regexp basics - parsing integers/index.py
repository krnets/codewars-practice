# 6kyu - Regexp basics - parsing integers

""" Implement a function, which should return an integer if the input string is in one of the formats specified below, 
or None otherwise.

Format:

    Optional - or +
    Base prefix 0b (binary), 0x (hexadecimal), 0o (octal), or in case of no prefix decimal.
    Digits depending on base

Any extra character (including whitespace) makes the input invalid, in which case you should return None.

Digits are case insensitive, but base prefix must be lower case.

See the test cases for examples. """

import re

# def to_integer(string):
#     if not re.match('\A(-?0x[0-9a-fA-F]+$)|(-?0b[01]+$)|(^-?0o[0-7]+$)|(^[-+]?\d+$)\Z', string):
#         return None
#     elif re.match('^0b', string):
#         return int(string[2:], 2)
#     elif re.match('^-0b', string):
#         return -int(string[3:], 2)
#     elif re.match('^0o', string):
#         return int(string[2:], 8)
#     elif re.match('^-0o', string):
#         return -int(string[3:], 8)
#     elif re.match('^0x', string):
#         return int(string[2:], 16)
#     elif re.match('^-0x', string):
#         return -int(string[3:], 16)
#     else:
#         return int(string)


def to_integer(string):
    if re.match('\A[+-]?(\d+|0b[01]+|0o[0-7]+|0x[0-9a-fA-F]+)\Z', string):
        return int(string, 10 if string[1:].isdigit() else 0)


q = to_integer("0x1e1"), 481
q
q = to_integer("0x1ed"), 493
q
q = to_integer("123"), 123
q
q = to_integer("0x123"), 0x123
q
q = to_integer("0o123"), 0o123
q
q = to_integer("0123"), 123
q
q = to_integer("0b1010"), 0b1010
q
q = to_integer("+123"), 123
q
q = to_integer("-123"), -123
q
q = to_integer("-0x123"), -0x123
q
q = to_integer("-0o123"), -0o123
q
q = to_integer("-0123"), -123
q
q = to_integer("-0b1010"), -0b1010
q
q = to_integer("0xDEADbeef"), 0xDEADBEEF
q
q = to_integer("123 "), None
q
q = to_integer(" 123"), None
q
q = to_integer("123\n"), None
q
q = to_integer("\n123"), None
q
q = to_integer("0X123"), None
q
q = to_integer("0O123"), None
q
q = to_integer("0o18"), None
q
q = to_integer("0B1010"), None
q
q = to_integer("0b12"), None
q
