# 7kyu - Finding length of the sequence

""" As part of this Kata, you need to find the length of the sequence in an array, 
between the first and the second occurrence of a specified number.

For example, for a given array arr

[0, -3, 7, 4, 0, 3, 7, 9]

Finding length between two 7s like

length_of_sequence([0, -3, 7, 4, 0, 3, 7, 9], 7)

would return 5.

For sake of simplicity, there will only be numbers (positive or negative) in the supplied array.

If there are less or more than two occurrences of the number to search for, return 0."""


def length_of_sequence(arr, n):
    return len(arr) - arr[::-1].index(n) - arr.index(n) if arr.count(n) == 2 else 0


q = length_of_sequence([1, 1], 1)  # 2
q
q = length_of_sequence([1, 2, 3, 1], 1)  # 4
q
q = length_of_sequence([-7, 5, 0, 2, 9, 5], 10)  # 0
q
q = length_of_sequence([-7, 5, 0, 2, 9, 5], 5)  # 5
q
q = length_of_sequence([-7, 6, 2, -7, 4], -7)  # 4
q
q = length_of_sequence(
    [1, 5, 1, 3, -2, 5, 1, 4, -5, 3, 3, 1, 3, 3, -2], 4)  # 0
q
q = length_of_sequence([-2, -3, 3, -3, -1, 3, -3, 0, -5, -5, -5, -2], 3)  # 4
q
