# 7kyu - regex validation of 24 hours time

""" Write a regex to validate a 24 hours time string. 

Accepted: 01:00 - 1:00
Not accepted: 24:00

You should check for correct length and no spaces. """

import re

# def validate_time(time):
#     return bool(re.findall('(\A(2?[0-3]|[0-1]?\d):[0-5]\d\Z)', time))

def validate_time(time):
    return bool(re.match('^(2[0-3]|[01]?\d):[0-5]\d$', time))


q = validate_time('1:00'), True
q
q = validate_time('1:00'), True
q
q = validate_time('13:1'), False
q
q = validate_time('12:60'), False
q
q = validate_time('12: 60'), False
q
q = validate_time('24:00'), False
q
q = validate_time('00:00'), True
q
q = validate_time('24o:00'), False
q
q = validate_time('24:000'), False
q
q = validate_time(''), False
q
q = validate_time('09:00'), True
q
q = validate_time('2400'), False
q
q = validate_time('foo12:00bar'), False
q
q = validate_time('010:00'), False
q
q = validate_time('1;00'), False
q
