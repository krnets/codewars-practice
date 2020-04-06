# 6kyu - Count and Group Character Occurrences in a String

""" Write a method that takes a string as an argument and groups the number of time each character appears 
in the string as a hash sorted by the highest number of occurrences.

The characters should be sorted alphabetically e.g:

get_char_count("cba") == {1: ["a", "b", "c"]}

You should ignore spaces, special characters and count uppercase letters as lowercase ones.

For example:

get_char_count("Mississippi")           ==  {4: ["i", "s"], 2: ["p"], 1: ["m"]}
get_char_count("Hello. Hello? HELLO!")  ==  {6: ["l"], 3: ["e", "h", "o"]}
get_char_count("aaa...bb...c!")         ==  {3: ["a"], 2: ["b"], 1: ["c"]}
get_char_count("abc123")                ==  {1: ["1", "2", "3", "a", "b", "c"]}
get_char_count("aaabbbccc")             ==  {3: ["a", "b", "c"]} """

# from collections import Counter, defaultdict

# def invert_dict(d):
#     d_inv = defaultdict(list)
#     for k, v in d.items():
#         d_inv[v].append(k)
#     return d_inv

# def get_char_count(s):
#     chars = [c for c in s.lower() if c.isalnum()]
#     freq = Counter(chars)
#     inverted = dict(invert_dict(freq))
#     for x in inverted:
#         inverted[x] = sorted(inverted[x])
#     return inverted

# from collections import Counter, defaultdict

# def get_char_count(s):
#     freq = Counter(c for c in s.lower() if c.isalnum())
#     inverted = defaultdict(list)
#     for k, v in freq.items():
#         inverted[v].append(k)
#     for x in inverted:
#         inverted[x] = sorted(inverted[x])
#     return dict(inverted)

from collections import Counter, defaultdict

def get_char_count(s):
    d = defaultdict(list)
    c = Counter(sorted(s.lower()))
    for k, v in c.items():
        if k.isalnum():
            d[v].append(k)
    return dict(d)


q = get_char_count("Mississippi")  # {4: ["i", "s"], 2: ["p"], 1: ["m"]}
q
q = get_char_count("Hello. Hello? HELLO!")  # {6: ["l"], 3: ["e", "h", "o"]}
q
q = get_char_count("aaa...bb...c!")  # {3: ["a"], 2: ["b"], 1: ["c"]}
q
q = get_char_count("abc123")  # {1: ["1", "2", "3", "a", "b", "c"]}
q
q = get_char_count("aaabbbccc")  # {3: ["a", "b", "c"]}
q
