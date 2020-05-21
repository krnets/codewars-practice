# 7kyu - Strong password?

""" Your users passwords were all stole in the Yahoo! hack, and it turns out they have been lax in creating secure passwords. 
Create a function that checks their new password (passed as a string) to make sure it meets the following requirements:

Between 8 - 20 characters

Contains only the following characters: (and at least one character from each category): 
uppercase letters, lowercase letters, digits, and the special characters !@#$%^&*?

Return "valid" if passed or else "not valid" """

import re

PATTERN = re.compile(
    '^'                    # begin string
    '(?=.*?[A-Z])'         # at least one uppercase letter
    '(?=.*?[a-z])'         # at least one lowercase letter
    '(?=.*?\d)'            # at least one digit
    '(?=.*?[!@#$%^&*?])'   # at least one special character
    '[A-Za-z\d!@#$%^&*?]'  # only the given characters
    '{8,20}'               # between 8 and 20 characters long
    '$'                    # end string
)

def check_password(s):
    return 'valid' if PATTERN.match(s) else 'not valid'

# def check_password(s):
#     return 'valid' if re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*?])[A-Za-z\d!@#$%^&*?]{8,20}$', s) else 'not valid'


q = check_password("P1@pP1@p")  # "valid"
q
q = check_password("Paaaaaa222!!!")  # "valid"
q
q = check_password("")  # "not valid"
q
q = check_password("password")  # "not valid"
q
q = check_password("P1@p")  # "not valid"
q
q = check_password("P1@pP1@pP1@pP1@pP1@pP1@p")  # "not valid"
q
