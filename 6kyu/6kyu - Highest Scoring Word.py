# 6kyu - Highest Scoring Word

""" Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid. """

# def high(x):
#     words = x.split()
#     score = []
#     for w in words:
#         char_vals = []
#         for i in range(len(w)):
#             char_vals.append(ord(w[i])-96)
#         score.append(sum(char_vals))
#     return words[score.index(max(score))]


def high(x):
    words = x.split()
    score = []
    for w in words:
        score.append(sum(ord(c)-96 for c in w))
    return words[score.index(max(score))]

# def high(x):
#     return max(x.split(), key=lambda w: sum(ord(c)-96 for c in w))


q = high('man i need a taxi up to ubud'), 'taxi'
q
q = high('what time are we climbing up the volcano'), 'volcano'
q
q = high('take me to semynak'), 'semynak'
q
