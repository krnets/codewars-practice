# 5kyu - Missing number in Unordered Arithmetic Progression

""" An Arithmetic Progression is defined as one in which there is a constant difference 
between the consecutive terms of a given series of numbers. 

You are provided with consecutive elements of an Arithmetic Progression. 
There is however one hitch: exactly one term from the original series is missing 
from the set of numbers which have been given to you.

The rest of the given series is the same as the original AP. 
Find the missing term in an unordered list. 

Try if you can survive lists of MASSIVE numbers (which means time limit should be considered).

Note: Don't be afraid that the minimum or the maximum element in the list is missing, 
e.g. [4, 6, 3, 5, 2] is missing 1 or 7, but this case is excluded from the kata.

find([3, 9, 1, 11, 13, 5]) # => 7 """


# def find(seq):
#     return (len(seq)+1) * (min(seq) + max(seq)) // 2 - sum(seq)

def find(seq):
    return (min(seq) + max(seq)) * (len(seq)+1) // 2 - sum(seq)


q = find([3, 9, 1, 11, 13, 5])  # 7
q
q = find([5, -1, 0, 3, 4, -3, 2, -2])  # 1
q
