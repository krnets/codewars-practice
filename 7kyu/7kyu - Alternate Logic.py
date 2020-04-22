# 7kyu - Alternate Logic

""" Create an OR function, without use of the 'or' keyword, that takes an list of 
boolean values and runs OR against all of them.

Assume there will be between 1 and 6 variables, and return None for an empty list. """

# from functools import reduce

# def alt_or(lst):
#     return reduce(lambda x, y: x | y, lst, False) if lst else None

# def alt_or(lst):
#     return any(lst) if lst else None

# def alt_or(lst):
#     return eval(str(lst).replace(',', ' |'))[0] if lst else None

def alt_or(lst):
    return bool(sum(lst)) if lst else None


q = alt_or([]), None
q
q = alt_or([False, False, False, False, True, True]), True
q
q = alt_or([False, True, False, True, False, True]), True
q
q = alt_or([True, False, True, False, True]), True
q
q = alt_or([False, False]), False
q
q = alt_or([False, True]), True
q
q = alt_or([True, False]), True
q
q = alt_or([True, True]), True
q
q = alt_or([False]), False
q
q = alt_or([True]), True
q
