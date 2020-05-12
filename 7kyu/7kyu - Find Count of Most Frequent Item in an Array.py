# 7kyu - Find Count of Most Frequent Item in an Array

""" Complete the function to find the count of the most frequent item of an array. 
You can assume that input is an array of integers. For an empty array return 0

input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5 

The most frequent number in the array is -1 and it occurs 5 times. """

from collections import Counter

# def most_frequent_item_count(collection):
#     return max([x for _, x in Counter(collection).items()], default=0)

def most_frequent_item_count(collection):
    return max(Counter(collection).values(), default=0)


q = most_frequent_item_count([3, -1, -1]), 2
q
q = most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]), 5
q
q = most_frequent_item_count([]), 0
q
q = most_frequent_item_count([9]), 1
q
