# Beta - Anagram or not

""" "Any word or phrase that exactly reproduces the letters in another order is an anagram." (Wikipedia). 
Add numbers to this definition to be more interest.

Examples of anagrams:

William Shakespeare = I am a weakish speller
silent = listen
12345 = 54321

The challenge is to write the function isAnagram to return True if the word test is an anagram of the word original 
and False if not.

Note: Anagrams are case insensitive, ignore all non-alphanumeric characters, input will always be two strings. 
Also: two identical words may be considered to be an edge case of an anagram, but for this kata they are still correct anagrams. """

import re

# def isAnagram(test, original):
#     aa = re.sub('\W', '', test.lower())
#     bb = re.sub('\W', '', original.lower())
#     return sorted(aa) == sorted(bb)


def isAnagram(test, original):
    canonical = lambda s: sorted(filter(str.isalnum, s.lower()))
    return canonical(test) == canonical(original)


q = isAnagram("7 c:5 /oof g;aqi!a8]", "(7-c:5 /oof g;aqi!a8]"), True
q
q = isAnagram("William Shakespeare", "I am a weakish speller"), True
q
q = isAnagram("Silent", "Listen"), True
q
q = isAnagram("Car", "Cat"), False, "Car is not an anagram of Cat"
q
q = isAnagram("12345", "54321"), True
q
