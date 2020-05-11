# 7kyu - Get Smallest Common Factor

""" Given an array of integers, return the smallest common factors of all integers in the array.

Smallest Common Factor means the smallest number above 1 that can divide all numbers in the array without a remainder.

scf([200, 30, 18, 8, 64, 34]) //=> 2
scf([21, 45, 51, 27, 33]) //=> 3
scf([133, 147, 427, 266]) //=> 7

If there are no common factors above 1, return 1 (technically 1 is always a common factor). """


def scf(arr):
    if arr:
        for i in range(2, min(arr)+1):
            if all(num % i == 0 for num in arr):
                return i
    return 1


q = scf([200, 30, 18, 8, 64, 34]), 2
q
q = scf([21, 45, 51, 27, 33]), 3
q
q = scf([133, 147, 427, 266]), 7
q
q = scf([3, 5, 7]), 1
q
q = scf([]), 1
q
