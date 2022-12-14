# 7kyu - Remove duplicate words

""" Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

Input: 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
Output: 'alpha beta gamma delta'  """


# def remove_duplicate_words(s):
#     seen = set()
#     words = []

#     for word in s.split():
#         if word not in seen:
#             words.append(word)
#             seen.add(word)

#     return " ".join(words)


def remove_duplicate_words(s):
    return " ".join(dict.fromkeys(s.split()))


# def remove_duplicate_words(s):
#     words = s.split()
#     return " ".join(sorted(set(words), key=words.index))

# from collections import OrderedDict

# def remove_duplicate_words(s):
#     return " ".join(OrderedDict.fromkeys(s.split()))


q = remove_duplicate_words(
    "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta")
q
#     alpha beta gamma delta
q = remove_duplicate_words("my cat is my cat fat")
q
#     my cat is fat
