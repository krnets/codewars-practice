# Beta - Find the non-unique number

""" Given a list of numbers, a number that appears only once is considered unique. 
The number that appears more than once is considered non-unique.

In this kata find the non-unique number and return a list consisting of two elements: 
[number, # of occurrences of the non-unique number]

If all the numbers in the list are unique, return the string 'unique'. 
If the list is empty, return the empty list [].

['1', '2', '3.0', '3'] -> [3, 2]
['0', '0.0', '0'] -> 'unique'
[] -> [] """

from collections import Counter

# def non_unique(lst):
#     if not lst:
#         return lst
#     freq = Counter([float(x) for x in lst])
#     for x in freq:
#         if freq[x] > 1:
#             if int(x) == x:
#                 return [int(x), freq[x]]
#             else:
#                 return [x, freq[x]]
#     return 'unique'

# def non_unique(lst):
#     if not lst:
#         return lst
#     freq = Counter(map(float, lst))
#     return 'unique' if len(freq) is len(lst) else list(freq.most_common(1)[0])


def non_unique(lst):
    if not lst:
        return lst
    freq = Counter(map(float, lst))
    return 'unique' if len(freq) is len(lst) else list(next(iter(freq.most_common())))


q = non_unique(['1', '2', '3', '4', '5', '5'])  # [5, 2]
q
q = non_unique(['1', '1', '1', '2'])  # [1, 3]
q
q = non_unique(['0', '0', '0', '0', '0', '0', '0.0', '0', '0', '0'])  # [0, 10]
q
q = non_unique(['2', '4', '6', '8', '10', '12', '14'])  # 'unique'
q
q = non_unique(['1', '1.25', '1.50', '1.75', '2.00', '2'])  # [2, 2]
q
q = non_unique(['0.25', '0.0', '0.01', '0.5', '0.50'])  # [0.5, 2]
q
q = non_unique(['-1.05', '1.05', '1.50', '1.5'])  # [1.5, 2]
q
q = non_unique([])  # []
q
