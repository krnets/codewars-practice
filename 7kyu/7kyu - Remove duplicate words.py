# 7kyu - Remove duplicate words

""" Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

Input: 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
Output: 'alpha beta gamma delta'  """


# def remove_duplicate_words(s):
#     arr = s.split()
#     return ' '.join(sorted(set(arr), key=arr.index))

def remove_duplicate_words(s):
    return ' '.join(dict.fromkeys(s.split()))


q = remove_duplicate_words(
    "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta")
q
#     "alpha beta gamma delta"
q = remove_duplicate_words("my cat is my cat fat")
q
#     "my cat is fat"
