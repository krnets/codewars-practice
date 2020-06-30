""" 5kyu - String incrementer

Write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered. """


import re

# def increment_string(strng):
#     last_digit = re.findall(r'\d+$', strng)
#     res = 1
#     n = 0
#     if last_digit and last_digit[0].isdigit():
#         res = int(last_digit[0]) + 1
#         n = len(last_digit[0])
#     return strng + str(res) if not last_digit else strng[:-n] + str(res).zfill(n)


def increment_string(strng):
    tail_digits = re.findall(r'\d+$', strng)
    n, inc = 0, 1
    if tail_digits:
        n = len(tail_digits[0])
        inc = int(tail_digits[0]) + 1
    return strng[:-n] + str(inc).zfill(n) if tail_digits else strng + str(inc)


q = increment_string("foo"), "foo1"
q
q = increment_string("foobar001"), "foobar002"
q
q = increment_string("foobar1"), "foobar2"
q
q = increment_string("foobar00"), "foobar01"
q
q = increment_string("foobar99"), "foobar100"
q
q = increment_string("foobar099"), "foobar100"
q
q = increment_string(""), "1"
q
