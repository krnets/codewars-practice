# 8kyu - Remove duplicates from list

""" Define a function that removes duplicates from an array of numbers and returns it as a result.

The order of the sequence has to stay the same. """


def distinct(seq):
    return list(dict.fromkeys(seq))

# def distinct(seq):
#     return sorted(set(seq), key=seq.index)


q = distinct([1])  # [1]
q
q = distinct([1, 2])  # [1, 2]
q
q = distinct([1, 1, 2])  # [1, 2]
q
q = distinct([1, 1, 1, 2, 3, 4, 5])  # [1, 2, 3, 4, 5]
q
q = distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7])  # [1, 2, 3, 4, 5, 6, 7]
q
