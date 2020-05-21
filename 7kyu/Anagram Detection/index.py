# 7kyu - Anagram Detection

""" An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

    "foefet" is an anagram of "toffee"

    "Buckethead" is an anagram of "DeathCubeK" """


# def is_anagram(test, original):
#     return sorted(test.lower()) == sorted(original.lower())

from collections import Counter

def is_anagram(test, original):
    return Counter(test.lower()) == Counter(original.lower())


q = is_anagram('Creative', 'Reactive')  # True
q
q = is_anagram("foefet", "toffee")  # True
q
q = is_anagram("Buckethead", "DeathCubeK")  # True
q
q = is_anagram("Twoo", "WooT")  # True
q
q = is_anagram("dumble", "bumble")  # False
q
q = is_anagram("ound", "round")  # False
q
q = is_anagram("apple", "pale")  # False
q
