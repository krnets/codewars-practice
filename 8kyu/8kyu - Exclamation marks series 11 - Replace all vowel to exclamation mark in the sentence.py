# 8kyu - Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence

""" Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.
Examples

replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"  """

import re

# def replace_exclamation(s):
#     pattern = re.compile('[aeiou]', re.IGNORECASE)
#     return re.sub(pattern, '!', s)

def replace_exclamation(s):
    return re.sub('[aeiouAEIOU]', '!', s)

# def replace_exclamation(s):
#     return s.translate(str.maketrans('aeiouAEIOU', '!' * 10))

q = replace_exclamation("Hi!")  # "H!!"
q
q = replace_exclamation("!Hi! Hi!")  # "!H!! H!!"
q
q = replace_exclamation("aeiou")  # "!!!!!"
q
q = replace_exclamation("ABCDE")  # "!BCD!"
q
