# 7kyu - Reverse words

""" Complete the function that accepts a string parameter, and reverses each word in the string. 
All spaces in the string should be retained.

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps" """

# def reverse_words(text):
#     words, spaces = [], []
#     word, res = "", ""
#     space_length = 0

#     for c in text:
#         if c == " ":
#             space_length += 1
#             if word != "":
#                 words.append(word)
#                 word = ""
#         else:
#             word += c
#             if space_length > 0:
#                 spaces.append(space_length)
#             space_length = 0

#     for i, space in enumerate(spaces):
#         res += words[i][::-1]
#         res += ' ' * space

#     return res + word[::-1]


# def reverse_words(text):
#     return " ".join(word[::-1] for word in text.split(" "))


import re


def reverse_words(text):
    return re.sub(r"\S+", lambda m: m.group(0)[::-1], text)


q = reverse_words("The quick brown fox jumps over the lazy dog.")
q
#    'ehT kciuq nworb xof spmuj revo eht yzal .god'
q = reverse_words("apple")  # 'elppa'
q
q = reverse_words("a b c d")  # 'a b c d'
q
q = reverse_words("double  spaced  words")
q
#    'elbuod  decaps  sdrow'
