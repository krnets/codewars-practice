# 6kyu - +1 Array

""" Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

    the array can't be empty
    only non-negative, single digit integers are allowed

Return nil (or your language's equivalent) for invalid inputs.

For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6] """

# def up_array(arr):
#     if not arr or any(x < 0 or x > 9 for x in arr):
#         return None
#     for i in range(len(arr) - 1, -1, -1):
#         if arr[i] < 9:
#             arr[i] += 1
#             return arr
#         else:
#             arr[i] = 0
#     return [1] + [0] * len(arr)

def up_array(arr):
    if arr and all(0 <= x <= 9 for x in arr):
        return list(map(int, str(int(''.join(map(str, arr)))+1)))


q = up_array([2, 3, 9])  # [2,4,0]
q
q = up_array([4, 3, 2, 5])  # [4,3,2,6]
q
q = up_array([1, -9])  # None
q
