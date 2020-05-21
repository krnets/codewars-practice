# 7kyu - Simple string division

""" In this Kata, you will be given a number in form of a string and an integer k.
Your task is to insert k commas into the string and determine which of the partitions is the largest.

solve('123',1) = 23 because we insert one comma and get the substrings ('1','23') or ('12',3). The max of these is '23'.
solve('1234',1) = 234 because ('1','234') or ('12','34') or ('123','4').
solve('1234',2) = 34 because ('1','2','34') or ('1','23','4') or ('12','3','4'). 
solve('1234',3) = 4. """


# def solve(st, k):
#     arr = []
#     for i in range(len(st)):
#         arr.append(int(st[i: i+(len(st)-k)]))
#     return max(arr)

def solve(st, k):
    length = len(st)-k
    return max(int(st[i:i+length]) for i in range(len(st)))

# from itertools import combinations
# from itertools import permutations

# def solve(st, k):
#     ans = 0
#     for pos in combinations(range(1, len(st)), k):
#         pos = list(pos)
#         ans = max(ans, max([int(st[a:b])
#                             for a, b in zip([0] + pos, pos + [len(st)])]))
#     return ans
#     # return list(combinations(st, k))
#     # return list(permutations(st, k))


q = solve('123', 1)  # 23
q
q = solve('1234', 1)  # 234
q
q = solve('1234', 2)  # 34
q
q = solve('1234', 3)  # 4
q
