""" 7kyu - Integer Difference

Write a function that accepts two arguments: an array of integers and another integer n.
Determine the number of times where two integers in the array have a difference of n.

int_diff([1, 1, 5, 6, 9, 16, 27], 4) # 3 ([1, 5], [1, 5], [5, 9])
int_diff([1, 1, 3, 3], 2) # 4 ([1, 3], [1, 3], [1, 3], [1, 3])

Note: your code should not modify the input array.  """

# def int_diff(lst, n):
#     count = 0
#     for i in range(1, len(lst)):
#         j = 0
#         while j < i:
#             if abs(lst[i] - lst[j]) == n:
#                 count += 1
#             j += 1
#     return count

# def int_diff(lst, n):
#     count = 0
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if abs(lst[i]-lst[j]) == n:
#                 count += 1
#     return count

# def int_diff(lst, n):
#     return sum(n == abs(a - b) for i, a in enumerate(lst) for b in lst[:i])

from itertools import combinations

# def int_diff(lst, n):
#     return len([(x, y) for x, y in combinations(lst, 2) if abs(x - y) == n])

def int_diff(lst, n):
    return sum(n == abs(x-y) for x, y in combinations(lst, 2))


q = int_diff([1, 1, 5, 6, 9, 16, 27], 4), 3
q
q = int_diff([1, 1, 3, 3], 2), 4
q
