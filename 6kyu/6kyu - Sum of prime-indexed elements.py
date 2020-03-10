# 6kyu - Sum of prime-indexed elements

""" In this Kata, you will be trained on array indexing and basic prime number operations. 
Array indices are zero-based; this means that the first element of an array is at index 0.

You will be given an integer array and your task is to return the sum of elements occupying prime-numbered indices.

To make this interesting, array lengths in random tests will have up to 5000 elements. """

from math import sqrt

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n >= 2

# def is_prime(n):
#     return n > 1 and all(n % i for i in range(2, int(n ** .5) + 1))

def total(arr):
    return sum(n for i, n in enumerate(arr) if is_prime(i))


q = total([])  # 0
q
q = total([1, 2, 3, 4])  # 7
q
q = total([1, 2, 3, 4, 5, 6])  # 13
q
q = total([1, 2, 3, 4, 5, 6, 7, 8])  # 21
q
q = total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])  # 21
q
q = total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])  # 33
q
q = total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])  # 47
q
