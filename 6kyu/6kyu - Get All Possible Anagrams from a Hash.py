# 6kyu - Get All Possible Anagrams from a Hash

""" Given a hash of letters and the number of times they occur, recreate all of the possible 
anagram combinations that could be created using all of the letters, sorted alphabetically.

The inputs will never include numbers, spaces or any special characters, only lowercase letters a-z.

get_words({2=>["a"], 1=>["b", "c"]}) => 
["aabc", "aacb", "abac", "abca", "acab", "acba", "baac", "baca", "bcaa", "caab", "caba", "cbaa"] """

# from pandas.core.common import flatten
# from itertools import permutations

# def get_words(hash_of_letters):
#     letters = flatten(vals * key for key, vals in hash_of_letters.items())
#     return sorted(set(''.join(x) for x in permutations(letters)))

from itertools import chain, permutations

def get_words(hash_of_letters):
    return sorted(set(''.join(x) for x in permutations(chain.from_iterable(v * k for (k, v) in hash_of_letters.items()))))


q = get_words({1: ["a", "b", "c"]})
q
#  ["abc", "acb", "bac", "bca", "cab", "cba"]

q = get_words({2: ["a"], 1: ["b", "c"]})
q
#  ["aabc", "aacb", "abac", "abca", "acab", "acba", "baac", "baca", "bcaa", "caab", "caba", "cbaa"]
