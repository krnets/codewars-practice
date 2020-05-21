# 7kyu - Is valid identifier?

""" Given a string, determine if it's a valid identifier.

##Here is the syntax for valid identifiers:

    Each identifier must have at least one character.
    The first character must be picked from: alpha, underscore, or dollar sign. 
    The first character cannot be a digit.
    The rest of the characters (besides the first) can be from: alpha, digit, underscore, or dollar sign. 
    In other words, it can be any valid identifier character.

###Examples of valid identifiers:
    i
    wo_rd
    b2h

###Examples of invalid identifiers:
    1i
    wo rd
    !b2h  """

import re

def is_valid(idn):
    return bool(re.match('^[a-z_$][\w_$]*$', idn, re.I))


q = is_valid("b$S")  # True
q
q = is_valid("Ne")  # True
q
q = is_valid("INi10x")  # True
q
q = is_valid("okay_ok1")  # True
q
q = is_valid("$ok")  # True
q
q = is_valid("___")  # True
q
q = is_valid("str_STR")  # True
q
q = is_valid("myIdentf")  # True
q
q = is_valid("1ok0okay")  # False
q
q = is_valid("!Ok")  # False
q
q = is_valid("")  # False
q
q = is_valid("str-str")  # False
q
q = is_valid("no no")  # False
q
q = is_valid("]")  # False
q
