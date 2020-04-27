# 7kyu - Exclamation marks series #5: Remove all exclamation marks from the end of words

""" Remove all exclamation marks from the end of words. Words are separated by spaces in the sentence.

remove("Hi!") === "Hi"
remove("Hi!!!") === "Hi"
remove("!Hi") === "!Hi"
remove("!Hi!") === "!Hi"
remove("Hi! Hi!") === "Hi Hi"
remove("!!!Hi !!hi!!! !hi") === "!!!Hi !!hi !hi" """

import re

def remove(s):
    return re.sub(r'\b\!+', '', s)


q = remove('Hi!')  # 'Hi'
q
q = remove('Hi!!!')  # 'Hi'
q
q = remove('!Hi')  # '!Hi'
q
q = remove('!Hi!')  # '!Hi'
q
q = remove('Hi! Hi!')  # 'Hi Hi'
q
q = remove('!!!Hi !!hi!!! !hi')  # '!!!Hi !!hi !hi'
q
