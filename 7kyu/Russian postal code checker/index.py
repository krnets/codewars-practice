# 7kyu - Russian postal code checker

""" You should write a simple function that takes string as input and checks if it is 
a valid Russian postal code, returning true or false.

A valid postcode should be 6 digits with no white spaces, letters or other symbols. 
Empty string should also return false.

Please also keep in mind that a valid post code cannot start with 0, 5, 7, 8 or 9

Valid postcodes:

    198328
    310003
    424000

Invalid postcodes:

    056879
    12A483
    1@63
    111 """

import re

# def zipvalidate(postcode):
#     return bool(re.match(r'^[12346]\d{5}$', postcode)) and all(x.isdigit() for x in postcode)

def zipvalidate(postcode):
    return bool(re.fullmatch('[12346]\d{5}', postcode))


q = zipvalidate('198328'), True
q
q = zipvalidate('310003'), True
q
q = zipvalidate('424000'), True
q
q = zipvalidate('12A483'), False
q
q = zipvalidate('1@63'), False
q
q = zipvalidate('111'), False
q
q = zipvalidate('056879'), False
q
q = zipvalidate('1111111'), False
q
