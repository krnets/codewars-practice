# def absent_vowel(x):
#     vowels = "AEIOU"
#     vowels_set = set(vowels)
#     x_vowels_only = set(filter(lambda c: c in vowels_set, x.upper()))

#     for i, vowel in enumerate(vowels):
#         if vowel not in x_vowels_only:
#             return i
#     return -1


def absent_vowel(x):
    vowels = "AEIOU"
    diff_set = set(vowels).difference(x.upper())
    return vowels.index(diff_set.pop())
