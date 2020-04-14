# 6kyu - Anagram difference

""" Given two words, how many letters do you have to remove from them to make them anagrams?
Example

    First word : codewars (4 letters removed)
    Second word : hackerrank (6 letters removed)
    Result : 10

Hints

    A word is an anagram of another word if they have the same letters (usually in a different order).
    Do not worry about case. All inputs will be lowercase.
    When you're done with this kata, check out its big brother/sister : https://www.codewars.com/kata/hardcore-anagram-difference """

from collections import Counter

# def anagram_difference(w1, w2):
#     diff = 0
#     count_w1 = Counter(w1)
#     count_w2 = Counter(w2)

#     for key in count_w1:
#         if key in count_w2:
#             count_w2[key] = count_w1[key] - count_w2[key]
#         else:
#             count_w2[key] = count_w1[key]

#     for key in count_w2:
#         diff += abs(count_w2[key])

#     return diff

def anagram_difference(w1, w2):
    c1 = Counter(w1)
    c1.subtract(w2)
    return sum(map(abs, c1.values()))


# def anagram_difference(w1, w2):
#     c1, c2 = Counter(w1), Counter(w2)
#     return sum(((c1 - c2) + (c2 - c1)).values())

# def anagram_difference(w1, w2):
#     c1, c2 = Counter(w1), Counter(w2)
#     return sum((c1 - c2).values()) + sum((c2 - c1).values())


q = anagram_difference('', '')  # 0
q
q = anagram_difference('a', '')  # 1
q
q = anagram_difference('', 'a')  # 1
q
q = anagram_difference('ab', 'a')  # 1
q
q = anagram_difference('ab', 'ba')  # 0
q
q = anagram_difference('ab', 'cd')  # 4
q
q = anagram_difference('codewars', 'hackerrank')  # 10
q