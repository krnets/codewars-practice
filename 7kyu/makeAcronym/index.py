# 7kyu - makeAcronym

""" Implement a function called makeAcronym that returns the first letters of each word in a passed in string.

Make sure the letters returned are uppercase.
If the value passed in is not a string return 'Not a string'.
If the value passed in is a string which contains characters other than spaces and alphabet letters, return 'Not letters'.
If the string is empty, just return the string itself: "".


'Hello codewarrior' -> 'HC'
'a42' -> 'Not letters'
42 -> 'Not a string'
[2,12] -> 'Not a string'
{name: 'Abraham'} -> 'Not a string' """

import re

def make_acronym(phrase):
    if not isinstance(phrase, str):
        return 'Not a string'
    elif re.findall('[^a-z\s]', phrase, re.I):
        return 'Not letters'
    return ''.join(word[0] for word in phrase.upper().split())


q = make_acronym('My aunt sally'), 'MAS'
q
q = make_acronym('Please excuse my dear aunt Sally'), 'PEMDAS'
q
# 'HMWWAWCIAWCCW'
q = make_acronym('How much wood would a woodchuck chuck if a woodchuck could chuck wood')
q
q = make_acronym('a42')  # 'Not letters'
q
q = make_acronym(42)  # 'Not a string'
q
q = make_acronym([2, 12])  # 'Not a string'
q
q = make_acronym({'name': 'Abraham'})  # 'Not a string'
q
