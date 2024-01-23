# def solve(arr):
#     res = []
#     max_so_far = -1
#     for x in reversed(arr):
#         if x > max_so_far:
#             res.append(x)
#             max_so_far = x
#     return res[::-1]


from itertools import accumulate

def solve(arr):
    return list(reversed(dict.fromkeys(accumulate(reversed(arr), max)).keys()))
