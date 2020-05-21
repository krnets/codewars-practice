# 7kyu - Simple Fun #68: Palindrome Rearranging

""" Given a string s, find out if its characters can be rearranged to form a palindrome.

For s = "aabb", the output should be true.

We can rearrange "aabb" to make "abba", which is a palindrome.

    [input] string s
    A string consisting of lowercase English letters.

    Constraints:
    4 ≤ inputString.length ≤ 50.

    [output] a boolean value
    true if the characters of the inputString can be rearranged to form a palindrome, false otherwise. """

from collections import Counter

# def palindrome_rearranging(s):
#     char_count = Counter(s)
#     return len([char_count[x] for x in char_count if char_count[x] % 2 != 0]) < 2


def palindrome_rearranging(s):
    return sum(n % 2 for n in Counter(s).values()) < 2

# def palindrome_rearranging(s):
#     return sum(s.count(c) % 2 for c in set(s)) < 2


q = palindrome_rearranging("aabb")  # True
q
q = palindrome_rearranging("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc")  # False
q
q = palindrome_rearranging("abbcabb")  # True
q
q = palindrome_rearranging("zyyzzzzz")  # True
q
