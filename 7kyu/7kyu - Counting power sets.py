# 7kyu - Counting power sets

""" In this kata, create a function powers/Powers that takes an array, and returns the number of subsets possible 
to create from that list. In other words, counts the power sets.

powers([1,2,3]) => 8

...due to...

powers([1,2,3]) =>
[[],
 [1],
 [2],
 [3],
 [1,2],
 [2,3],
 [1,3],
 [1,2,3]]

Your function should be able to count sets up to the size of 500, so watch out; pretty big numbers occur there!
For comparison, my Haskell solution can compute the number of sets for an array of length 90 000 in less than a second, 
so be quick!
You should treat each array passed as a set of unique values for this kata. """


# def powers(lst):
#     return pow(2, len(lst))

def powers(lst):
    return 2 ** len(lst)

q = powers([])  # 1
q
q = powers([1])  # 2
q
q = powers([1, 2])  # 4
q
q = powers([1, 2, 3])  # 8
q
q = powers([1, 2, 3, 4])  # 16
q
