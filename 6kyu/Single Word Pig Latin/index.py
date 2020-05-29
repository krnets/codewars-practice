# 6kyu - Single Word Pig Latin

""" Pig Latin is an English language game where the goal is
to hide the meaning of a word from people not aware of the rules.

The rules themselves are rather easy:

1) The word starts with a vowel(a,e,i,o,u) -> return the original string plus "way".

2) The word starts with a consonant -> move consonants from the beginning of the word
to the end of the word until the first vowel, then return it plus "ay".

3) The result must be lowercase, regardless of the case of the input.
If the input string has any non-alpha characters, the function must return None.

4) The function must also handle simple random strings and not just English words.

5) The input string has no vowels -> return the original string plus "ay".

For example, the word "spaghetti" becomes "aghettispay" because the first two letters ("sp")
are consonants, so they are moved to the end of the string and "ay" is appended. """


import re


def pig_latin(text):
    text = text.lower()
    if not text or bool(re.findall(r'\d', text)):
        return None
    if re.match(r'^[aeiou]', text):
        return text + "way"
    for i in range(len(text)):
        if re.match(r'^[aeiou]', text):
            return text + "ay"
        text = text[1:] + text[0]
    return text + "ay"


q = pig_latin('es3t5tay'), None
q
q = pig_latin('ay'),  None
q
q = pig_latin('a1yay'),  None
q

q = pig_latin("map"), "apmay"
q
q = pig_latin("egg"), "eggway"
q
q = pig_latin("spaghetti"), "aghettispay"
q
