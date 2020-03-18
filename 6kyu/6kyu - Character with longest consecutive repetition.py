# 6kyu - Character with longest consecutive repetition

""" For a given string s find the character c (or C) with longest consecutive repetition and return:

(c, l)

where l (or L) is the length of the repetition. 
If there are two or more characters with the same l return the first.

For empty string return:

('', 0) """


# from itertools import groupby

# def longest_repetition(chars):
#     if len(chars) == 0:
#         return ('', 0)
#     groups = [list(g) for _, g in groupby(chars)]
#     longest = max(len(x) for x in groups)
#     return next((x[0], len(x)) for x in groups if len(x) == longest)


# def longest_repetition(chars):
#     if not chars: return ('', 0)
#     groups = [list(g) for _, g in groupby(chars)]
#     longest = max(len(x) for x in groups)
#     return next((x[0], len(x)) for x in groups if len(x) == longest)

# def longest_repetition(chars):
#     ch, count = '', 0
#     max_ch, max_count = '', 0
#     for c in chars:
#         if c != ch:
#             count, ch = 0, c
#         count += 1
#         if count > max_count:
#             max_ch, max_count = ch, count
#     return max_ch, max_count

# import re

# def longest_repetition(chars):
#     if not chars:
#         return ('', 0)
#     longest = max(re.findall(r'((.)\2*)', chars), key=lambda x: len(x[0]))
#     return longest[1], len(longest[0])

from itertools import groupby

def longest_repetition(chars):
    matches = [(c, len(list(g))) for c, g in groupby(chars)]
    return max(matches, key=lambda x: x[1], default=('', 0))

# from itertools import groupby
# from operator import itemgetter

# def longest_repetition(chars):
#     matches = [(c, len(list(g))) for c, g in groupby(chars)]
#     return max(matches, key=itemgetter(1), default=('', 0))


q = longest_repetition("aaaabb")  # ('a', 4)
q
q = longest_repetition("bbbaaabaaaa")  # ('a', 4)]
q
q = longest_repetition("cbdeuuu900")  # ('u', 3)
q
q = longest_repetition("abbbbb")  # ('b', 5)
q
q = longest_repetition("aabb")  # ('a', 2)
q
q = longest_repetition("ba")  # ('b', 1)
q
q = longest_repetition("")  # ('', 0)
q
