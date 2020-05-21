# 8kyu - Simple validation of a username with regex

""" Write a simple regex to validate a username. Allowed characters are:

    lowercase letters,
    numbers,
    underscore

Length should be between 4 and 16 characters (both included). """

# from re import match

import re

def validate_usr(username):
    return bool(re.match('^[a-z0-9_]{4,16}$', username))


q = validate_usr('asddsa')  # True
q
q = validate_usr('a')  # False
q
q = validate_usr('Hass')  # False
q
q = validate_usr('Hasd_12assssssasasasasasaasasasasas')  # False
q
q = validate_usr('')  # False
q
q = validate_usr('____')  # True
q
q = validate_usr('012')  # False
q
q = validate_usr('p1pp1')  # True
q
q = validate_usr('asd43 34')  # False
q
q = validate_usr('asd43_34')  # True
q
