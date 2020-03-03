# 8kyu - Sum Arrays

""" Write a method sum_array in python that takes an array of numbers and returns the sum of the numbers. 
The numbers can also be negative. If the array does not contain any numbers then you should return 0.

Assumptions

    You can assume that you are only given numbers.
    You cannot assume the size of the array.
    You can assume that you do get an array and if the array is empty, return 0. """


def sum_array(a):
    return sum(a)

# sum_array = sum


q = sum_array([])  # 0
q
q = sum_array([1, 2, 3])  # 6
q
q = sum_array([1.1, 2.2, 3.3])  # 6.6
q
q = sum_array([4, 5, 6])  # 15
q
q = sum_array(range(101))  # 5050
q
