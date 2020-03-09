# 7kyu - Counting Array Elements

""" Write a function that takes an array and counts the number of each unique element present.

count(['james', 'james', 'john']) 
#=> { 'james' => 2, 'john' => 1} """

# from collections import Counter

# def count(array):
#     return Counter(array)

from collections import Counter as count

q = count(['a', 'a', 'b', 'b', 'b'])  # { 'a': 2, 'b': 3 })
q
