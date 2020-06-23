""" 7kyu - Coding 3min : A*B=C

Give you a number array numbers and a number c.

Find out a pair of numbers(we called them number a and number b) 
from the array numbers, let a*b=c, result format is an array [a,b]

The array numbers is a sorted array, value range: -100...100

The result will be the first pair of numbers, for example,
findAB([1,2,3,4,5,6],6) should return [1,6], instead of [2,3]

Please see more example in testcases. """


# def find_a_b(numbers, c):
#     for i, a in enumerate(numbers, 1):
#         for b in numbers[i:]:
#             if a * b == c:
#                 return [a, b]

from collections import Counter

def find_a_b(numbers, c):
    count = Counter(numbers)
    for a in numbers:
        if a and c % a == 0:
            b = c // a
            if (a == b and count[b] >= 2) or (a != b and count[b] >= 1):
                return [a, b]


q = find_a_b([1, 2, 3], 3), [1, 3]
q
q = find_a_b([1, 2, 3], 6), [2, 3]
q
q = find_a_b([1, 2, 3], 7), None
q
q = find_a_b([1, 2, 3, 6], 6), [1, 6]
q
q = find_a_b([1, 2, 3, 4, 5, 6], 15), [3, 5]
q
q = find_a_b([0, 0, 2], 4), None
q
q = find_a_b([0, 0, 2, 2], 4), [2, 2]
q
q = find_a_b([-3, -2, -2, -1, 0, 1, 2, 3, 4], 4), [-2, -2]
q
q = find_a_b([-3, -2, -2, -1, 0, 1, 2, 3, 4], 0), [-3, 0]
q
q = find_a_b([-3, -2, -1, 0, 1, 2, 3, 4], 4), [1, 4]
q
