# Beta - Email Validation

""" Write a function to test whether a given input is a valid email address.

For the purposes of this kata, here is what makes a valid email:

    At least one letter character at the beginning
    All characters between the first character and the @ (if any) must be letters, numbers, or underscores
    There must be an @ character (after the points listed just now)
    After the @ character, there must be at least one word character (letter, number, or underscore) or hyphen
    The email must end with at least one set of a dot followed by one or more word characters.
    The input must NOT be case-sensitive

The function should return true or false. """

import re

def validate(input):
    return bool(re.match(r'[a-z]\w*@[a-z\-\_\d]+(\.\w{1,})+$', input))


q = validate('abc@example.com')  # True
q
q = validate('_bc@example.com')  # False
q
