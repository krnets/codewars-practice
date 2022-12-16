# 7kyu - Two Oldest Ages

""" The two oldest ages function/method needs to be completed. 
It should take an array of numbers as its argument and return the two highest numbers within the array. 
The returned value should be an array in the format [second oldest age, oldest age].

The order of the numbers passed in could be any order. 
The array will always include at least 2 items.

two_oldest_ages([1, 3, 10, 0]) # should return [3, 10] """

# def two_oldest_ages(ages):
#     return sorted(ages)[-2:]

import heapq

def two_oldest_ages(ages):
    return sorted(heapq.nlargest(2, ages))


q = two_oldest_ages([1, 5, 87, 45, 8, 8])  # [45, 87]
q
q = two_oldest_ages([6, 5, 83, 5, 3, 18])  # [18, 83]
q
q = two_oldest_ages([10, 1])  # [1, 10]
q
q = two_oldest_ages([1, 2, 10, 8])  # [8, 10]
q
q = two_oldest_ages([1, 5, 87, 45, 8, 8])  # [45, 87]
q
q = two_oldest_ages([1, 3, 10, 0])  # [3, 10]
q
