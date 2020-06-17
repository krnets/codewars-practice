""" 7kyu - Make Your Own Hashmap

This function will take in a list of strings and put them into a hashmap. 
A hashmap is a quick way to store and lookup items you might need based on the 'hash' of the item.
https://en.wikipedia.org/wiki/Hash_table

In this example, we're going to create hashes based on the sum of the characters. 
Each charater has a decimal value (ascii value) and the sum of those decimal values will be the hash.

Your goal is to take the list of strings, hash them, and return a dictionary with hashes as keys 
and a list of strings, with that hash, as values. """

# def my_hash_map(list_of_strings):
#     res = {}
#     for st in list_of_strings:
#         hash = sum(ord(ch) for ch in st)
#         if hash in res:
#             res[hash].append(st)
#         else:
#             res[hash] = [st]
#     return resa

# from functools import reduce
# from collections import defaultdict

# def my_hash_map(list_of_strings):
#     return reduce(lambda h, s: h[sum(map(ord, s))].append(s) or h, list_of_strings, defaultdict(list))

# def my_hash_map(list_of_strings):
#     result = defaultdict(list)
#     for string in list_of_strings:
#         result[sum(ord(char) for char in string)].append(string)
#     return result

# def my_hash_map(list_of_strings):
#     dct = defaultdict(list)
#     for w in list_of_strings:
#         dct[sum(map(ord, w))].append(w)
#     return dct


def my_hash_map(list_of_strings):
    dct = {}
    for w in list_of_strings:
        dct.setdefault(sum(map(ord, w)), []).append(w)
    return dct


list_of_strings = ["alphabet"]
q = my_hash_map(list_of_strings), {833: ['alphabet']}
q

list_of_strings = ["alphabet", 'black', 'zr3tMwHFGVGQyPu', 'UXwi5pRt8tZYGXb',
                   'TpaQ74BfSCPCpoD', '7qLoMzFjdLnMWDe', 'xNRjuXUI5wwPRLG', 'JlPDtxHSd02qUwP', 'TzPahGcFIkKsFa4']
q = my_hash_map(list_of_strings)
q
#      {833: ['alphabet'], 509: ['black'], 1368: ['zr3tMwHFGVGQyPu', 'UXwi5pRt8tZYGXb'], 1237: ['TpaQ74BfSCPCpoD'], 1349: ['7qLoMzFjdLnMWDe', 'xNRjuXUI5wwPRLG'] 