""" 7kyu - Palindrome Pairs

Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list 
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

["bat", "tab", "cat"] # [[0, 1], [1, 0]]
["dog", "cow", "tap", "god", "pat"] # [[0, 3], [2, 4], [3, 0], [4, 2]]
["abcd", "dcba", "lls", "s", "sssll"] # [[0, 1], [1, 0], [2, 4], [3, 2]]

Non-string inputs should be converted to strings.

Return an array of arrays containing pairs of distinct indices that form palindromes. 
Pairs should be reutrned in the order they appear in the original list. """


# def palindrome_pairs(words):
#     indices = []
#     for i, x in enumerate(words):
#         for j, y in enumerate(words):
#             if i != j:
#                 combined = str(x) + str(y)
#                 if combined == combined[::-1]:
#                     indices.append([i, j])
#     return indices

def is_palindrome(word):
    return word == word[::-1]

def palindrome_pairs(words):
    return [[i, j]
            for i, word_i in enumerate(words)
            for j, word_j in enumerate(words)
            if i != j and is_palindrome(word_i + word_j)]


q = palindrome_pairs(["bat", "tab", "cat"])
q
#      [[0, 1], [1, 0]]
q = palindrome_pairs(["dog", "cow", "tap", "god", "pat"])
q
#      [[0, 3], [2, 4], [3, 0], [4, 2]]
q = palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
q
#      [[0, 1], [1, 0], [2, 4], [3, 2]]
