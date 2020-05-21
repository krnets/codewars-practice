# 7kyu - Sum of array singles

""" In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. 
Your task will be to return the sum of the numbers that occur only once.

For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. """

# def repeats(arr):
#     res = []
#     for x in arr:
#         if x not in res:
#             res.append(x)
#         elif x in res:
#             res.remove(x)
#     return sum(res)

# def repeats(arr):
#     res = []
#     [res.append(x) if x not in res else res.remove(x) for x in arr]
#     return sum(res)


# def repeats(arr):  # quadratic time complexity
#     return sum(x for x in arr if arr.count(x) == 1)

from collections import Counter

def repeats(arr):
    return sum(k for k, v in Counter(arr).items() if v == 1)


q = repeats([4, 5, 7, 5, 4, 8])  # 15
q
q = repeats([9, 10, 19, 13, 19, 13])  # 19
q
q = repeats([16, 0, 11, 4, 8, 16, 0, 11])  # 12
q
q = repeats([5, 17, 18, 11, 13, 18, 11, 13])  # 22
q
q = repeats([5, 10, 19, 13, 10, 13])  # 24
q
