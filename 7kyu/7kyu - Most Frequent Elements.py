# 7kyu - Most Frequent Elements

""" Find the most frequent element or elements in the list.

find_most_frequent([1, 1, 2, 3]) == set([1])
find_most_frequent([1, 1, 2, 2, 3]) == set([1, 2])
find_most_frequent([1, 1, '2', '2', 3]) == set([1, '2']) """

from collections import Counter

# def find_most_frequent(l):
#     result = []
#     maxsofar = 0
#     for k, v in Counter(l).items():
#         if v > maxsofar:
#             result = [k]
#             maxsofar = v
#         elif v == maxsofar:
#             result.append(k)
#     return set(result)


def find_most_frequent(l):
    c = Counter(l)
    return {key for key, value in c.items() if value == max(c.values())}


q = find_most_frequent([1, 1, 2, 3]), set([1])  # 'one most frequent element'
q
q = find_most_frequent([1, 1, 2, 2, 3]), set([1, 2])  # 'two most frequent element'
q
q = find_most_frequent([]), set([])  # 'empty'
q
