# 7kyu - How many are smaller than me?

# Write smaller(arr) that given an array arr, you have to return the amount of numbers that are smaller than arr[i] to the right.


# def smaller(arr):
#     res = []
#     for i in range(len(arr)-1):
#         right_slice = arr[i+1:]
#         count_if_smaller = len([x for x in right_slice if x < arr[i]])
#         res.append(count_if_smaller)
#     return res + [0]

# def smaller(arr):
#     return [len([a for a in arr[i:] if a < arr[i]]) for i in range(0, len(arr))]

def smaller(arr):
    return [sum(a > b for b in arr[i+1:]) for i, a in enumerate(arr)]


q = smaller([5, 4, 3, 2, 1])  # [4, 3, 2, 1, 0]
q
q = smaller([1, 2, 3])  # [0, 0, 0]
q
q = smaller([1, 2, 0])  # [1, 1, 0]
q
q = smaller([1, 2, 1])  # [0, 1, 0]
q
q = smaller([1, 1, -1, 0, 0])  # [3, 3, 0, 0, 0]
q
q = smaller([5, 4, 7, 9, 2, 4, 4, 5, 6])  # [4, 1, 5, 5, 0, 0, 0, 0, 0]
q
