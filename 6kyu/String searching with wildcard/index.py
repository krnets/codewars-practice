# 6kyu - String searching with wildcard

""" The method below, is the most simple string search algorithm. 
It will find the first occurrence of a word in a text string.

haystack = the whole text
needle = searchword
wildcard = _

find("strike", "i will strike down upon thee"); // return 7

The find method is already made.
The problem is to implement wildcard(s) in the needle. 
If you have a _ in the needle it will match any character in the haystack.
A normal string search algorithm will find the first occurrence of a word(needle) 
in a text(haystack), starting on index 0. Like this:

find("strike", "I will strike down upon thee"); return 7

A wildcard in the needle will match any character in the haystack. 
The method should work on any types of needle, and haystasks. 
You can assume the needle is shorter than(or equal to) the haystack.

find("g__d", "That's the good thing about being president"); // return 11

If no match the method should return -1 """

import re

# def find(needle, haystack):
#     needle = re.sub(r'[^a-zA-Z0-9.,-]', '.', needle)
#     pattern = re.compile(needle)
#     result = re.search(pattern, haystack)
#     if result:
#         return int(re.sub(r'\D', ' ', str(result)).split()[0])
#     else:
#         return -1

def find(needle, haystack):
    pattern = re.compile(re.escape(needle).replace('_', '.'))
    matches = re.search(pattern, haystack)
    return matches.start() if matches else -1


haystack = "Once upon a midnight dreary, while I pondered, weak and weary"

# "Normal Search
q = find("Once", haystack)  # 0
q
q = find("midnight", haystack)  # 12
q
q = find("codewars", haystack)  # -1
q

# "Wild Search
q = find("_po_", haystack)  # 5
q
q = find("___night", haystack)  # 12
q
q = find('_lexe', 'googgoogleggggoooglxeplexhexflexmexkex')  # -1
q
q = find('--_.,', '-..,.44$&%$--,.,')  # 11
q
q = find('-..,.44$&%$--,.,', '-..,.44$&%$--,.,')  # 0
q
q = find('___4$&%$--___', '-..,.44$&%$--,.,')  # 3
q
