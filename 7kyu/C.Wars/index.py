""" 7kyu - C.Wars

Normally we have firstname, middle and the last name but there may be more than one word in a name like a South Indian one.

Similar to those kinda names we need to initialize the names.

See the pattern below

initials('code wars') => returns C.Wars 
initials('Barack Hussain obama') => returns B.H.Obama 

Complete the function initials. """

import re

# def initials(name):
#     return '.'.join(re.findall(r'((?=\w+$)\w+|\w)\w*', name)).title()

def initials(name):
    return re.sub(r'(\S)\S* ', r'\1.', name).title()


q = initials('code wars'), 'C.Wars'
q
q = initials('Barack hussein obama'), 'B.H.Obama'
q
q = initials('barack hussein Obama'), 'B.H.Obama'
q
