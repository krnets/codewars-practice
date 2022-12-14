# 7kyu - Find the stray number

""" You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3 """

# from collections import Counter

# def stray(arr):
#     freq = Counter(arr)
#     for x in freq:
#         if freq[x] == 1:
#             return x

# def stray(arr):
#     return min(arr, key=arr.count)


# def stray(arr):
#     return [x for x in set(arr) if arr.count(x) == 1][0]

# from functools import reduce

# def stray(arr):
#     return reduce(lambda prev, cur: prev ^ cur, arr)

from functools import reduce

def stray(arr):
    return reduce(lambda p, c: p ^ c, arr)

q = stray([1, 1, 1, 1, 1, 1, 2])  # 2
q
q = stray([2, 3, 2, 2, 2])  # 3
q
q = stray([3, 2, 2, 2, 2])  # 3
q
q = stray([17, 17, 3, 17, 17, 17, 17])  # 3
q
q = stray([3, 2, 2, 2, 2])  # 3
q