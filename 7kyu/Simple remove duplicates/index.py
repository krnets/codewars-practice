# 7kyu - Simple remove duplicates

""" In this Kata, you will remove the left-most duplicates from a list of integers and return the result.

# Remove the 3's at indices 0 and 3
# followed by removing a 4 at index 1 """


# def solve(arr):
#     res = []
#     for i, v in enumerate(arr[::-1]):
#         if v not in res:
#             res.append(v)
#     return res[::-1]

def solve(arr):
    return list(dict.fromkeys(arr[::-1]))[::-1]


q = solve([3, 4, 4, 3, 6, 3])  # [4,6,3]
q
q = solve([1, 2, 1, 2, 1, 2, 3])  # [1,2,3]
q
q = solve([1, 2, 3, 4])  # [1,2,3,4]
q
q = solve([1, 1, 4, 5, 1, 2, 1])  # [4,5,2,1]
q
