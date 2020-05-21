# 7kyu - Sorting Dictionaries

""" Python dictionaries are inherently unsorted. 
So what do you do if you need to sort the contents of a dictionary?

Create a function that returns a sorted list of (key, value) tuples.
The list must be sorted by the value and be sorted largest to smallest.

sort_dict({3:1, 2:2, 1:3}) == [(1,3), (2,2), (3,1)]
sort_dict({1:2, 2:4, 3:6}) == [(3,6), (2,4), (1,2)] """


def sort_dict(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)


q = sort_dict({3: 1, 2: 2, 1: 3})  # [(1,3), (2,2), (3,1)]
q
q = sort_dict({1: 2, 2: 4, 3: 6})  # [(3,6), (2,4), (1,2)]
q
# [(3,10), (8,8), (1,5), (6,3), (2,2)]
q = sort_dict({1: 5, 3: 10, 2: 2, 6: 3, 8: 8})
q
