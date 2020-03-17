# 7kyu - Simple string division II

""" Consider the string "1 2 36 4 8". 
We want to take pairs of these numbers, concatenate each pair and determine how many of them of divisible by k.

If k = 3, we get following numbers ['12', '18', '21', '24', '42', '48', '81', '84'], all divisible by 3.   

-- 21 and 12 are different pairs. 
-- Elements must be from different indices, so '3636` is not a valid concatenated pair. 

Given a string of numbers and an integer k, return the number of pairs that when concatenated, are divisible by k.

solve("1 2 36 4 8", 3) = 8, because they are ['12', '18', '21', '24', '42', '48', '81', '84']
solve("1 3 6 3", 3) = 6. They are ['36', '33', '63', '63', '33', '36'] """

# def solve(s, k):
#     arr = s.split()
#     count = 0
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i is not j:
#                 if int(arr[i] + arr[j]) % k == 0:
#                     count += 1
#     return count

from itertools import permutations

# def solve(s, k):
#     return sum(int(v) % k == 0 for v in map(''.join, permutations(s.split(), 2)))

def solve(s, k):
    return sum(int(x + y) % k == 0 for x, y in permutations(s.split(), 2))


q = solve("1 2 36 4 8", 2)  # 16
q
q = solve("1 2 36 4 8", 3)  # 8
q
q = solve("1 2 36 4 8", 4)  # 11
q
q = solve("1 2 36 4 8", 8)  # 4
q
