# 7kyu - Sum a list but ignore any duplicates

""" Please write a function that sums a list, but ignores any duplicate items in the list.

For instance, for the list [3, 4, 3, 6] , the function should return 10. """

# from collections import Counter

# def sum_no_duplicates(l):
#     freq = Counter(l)
#     return sum(x for x in freq if freq[x] == 1)

# def sum_no_duplicates(l):
# return sum(k for k, v in Counter(l).items() if v == 1)

def sum_no_duplicates(l):
    return sum(v for v in set(l) if l.count(v) == 1)


q = sum_no_duplicates([1, 1, 2, 3])  # 5
q
q = sum_no_duplicates([1, 1, 2, 2, 3])  # 3
q
