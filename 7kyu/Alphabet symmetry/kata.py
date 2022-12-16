# def solve(arr):
#     res = []

#     for s in map(str.lower, arr):
#         count = sum(ord(c) - ord("a") == i for i, c in enumerate(s))
#         res.append(count)

#     return res

from string import ascii_lowercase as abc

def solve(arr):
    return [sum(abc[i % 26] == c for i, c in enumerate(s.lower())) for s in arr]


q = solve(["abode", "ABc", "xyzD"])  # [4,3,1]
q
q = solve(["abide", "ABc", "xyz"])  # [4,3,0]
q
q = solve(["IAMDEFANDJKL", "thedefgh", "xyzDEFghijabc"])  # [6,5,7]
q
q = solve(["encode", "abc", "xyzD", "ABmD"])  # [1, 3, 1, 3]
q
