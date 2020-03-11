# 7kyu - Partial Word Searching

""" Write a method that will search an array of strings for all strings that contain another string, 
ignoring capitalization. Then return an array of the found strings.

The method takes two parameters, the query string and the array of strings to search, and returns an array.

If the string isn't contained in any of the strings in the array, the method returns an array containing 
a single string: "Empty" (or Nothing in Haskell, or "None" in Python and C)

Example: If the string to search for is "me", and the array to search is ["home", "milk", "Mercury", "fish"], 
the method should return ["home", "Mercury"]. """

import re

# def word_search(query, seq):
#     res = [x for x in seq if re.search(query, x, re.I)]
#     return ['None'] if len(res) == 0 else res

# def word_search(query, seq):
#     res = [x for x in seq if re.search(query, x, re.I)]
#     return res if res else ['None']

def word_search(query, seq):
    return [x for x in seq if re.search(query, x, re.I)] or ['None']

# def word_search(query, seq):
#     return [x for x in seq if query.lower() in x.lower()] or ['None']


q = word_search("ab", ["za", "ab", "abc", "zab", "zbc"])
q
#      ["ab", "abc", "zab"]

q = word_search('me', ["home", "milk", "Mercury", "fish"])
q
#      ["home", "Mercury"]
