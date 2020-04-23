# 6kyu - Regexp basics - parsing time

""" Implement a function, which should parse time expressed as HH:MM:SS, or None otherwise.

Any extra characters, or minutes/seconds higher than 59 make the input invalid, and so should return None. """

import re
from functools import reduce

# def to_seconds(time):
#     if re.match(r'\A\d\d:[0-5]\d:[0-5]\d\Z', time):
#         hh, mm, ss = time.split(':')
#         return int(hh) * 60 * 60 + int(mm) * 60 + int(ss)

def to_seconds(time):
    if re.match(r'\A\d\d:[0-5]\d:[0-5]\d\Z', time):
        return reduce(lambda x, y: x * 60 + y, map(int, time.split(':')))


q = to_seconds("00:00:00"), 0
q
q = to_seconds("01:02:03"), 3723
q
q = to_seconds("01:02:60"), None
q
q = to_seconds("01:60:03"), None
q
q = to_seconds("99:59:59"), 359999
q
q = to_seconds("0:00:00"), None
q
q = to_seconds("00:0:00"), None
q
q = to_seconds("00:00:0"), None
q
q = to_seconds("00:00:00\n"), None
q
q = to_seconds("\n00:00:00"), None
q
