# 6kyu - Convert string to camel case

""" Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case).

to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"
to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior" """

import re

# def to_camel_case(text):
#     arr = re.sub(r'[-_]', ' ', text).split()
#     for i in range(1, len(arr)):
#         arr[i] = arr[i].capitalize()
#     return ''.join(arr)

# def to_camel_case(text):
#     arr = re.split(r'[-_]', text)
#     arr[1:] = map(str.capitalize, arr[1:])
#     return ''.join(arr)

# def to_camel_case(text):
#     arr = re.split('[_-]', text)
#     return ''.join(arr[:1] + [x.title() for x in arr[1:]])

# def to_camel_case(s):
#     return s[0] + s.title().translate({ord('-'): None, ord('_'): None})[1:] if s else s

def to_camel_case(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)


q = to_camel_case('')  # ''
q
q = to_camel_case("the_stealth_warrior")  # "theStealthWarrior"
q
q = to_camel_case("The-Stealth-Warrior")  # "TheStealthWarrior"
q
q = to_camel_case("A-B-C")  # "ABC"
q
