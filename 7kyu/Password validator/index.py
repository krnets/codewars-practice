# 7kyu - Password validator

""" Create a simple password validation function, as seen on many websites.
The rules for a valid password are as follows:

    There needs to be at least 1 uppercase letter.
    There needs to be at least 1 lowercase letter.
    There needs to be at least 1 number.
    The password needs to be at least 8 characters long.

You are permitted to use any methods to validate the password.

    You will only be passed strings.
    The string can contain any standard keyboard character.
    Accepted strings can be any length, as long as they are 8 characters or more. """

import re

# def password(string):
#     return len(re.findall(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.{8,})', string)) > 0

def password(string):
    return bool(re.match(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.{8,})', string))

# def password(string):
#     patterns = (r'[A-Z]', r'[a-z]', r'[0-9]', r'.{8,}')
#     return all([re.search(pattern, string) for pattern in patterns])


# CRITERIA = (str.islower, str.isupper, str.isdigit)

# def password(string):
#     return len(string) > 7 and all(any(map(fn, string)) for fn in CRITERIA)


q = password("Abcd1234")  # True
q
q = password("Abcd123")  # False
q
q = password("abcd1234")  # False
q
q = password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890")  # True
q
q = password("ABCD1234")  # False
q
q = password("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,")  # True
q
q = password("!@#$%^&*()-_+={}[]|\:;?/>.<,")  # False
q
q = password("")  # False
q
q = password(" aA1----")  # True
q
q = password("4aA1----")  # True
q
