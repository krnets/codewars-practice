# def min_value_array(arr):
#     res = []
#     for j in range(len(arr[0])):
#         col = []
#         for i in range(len(arr)):
#             col.append(arr[i][j])
#         res.append(min(col))
#     return res

import numpy as np


# def min_value_array(arr):
#     return [min(row) for row in np.rot90(arr, k=-1)]


# def min_value_array(arr):
#     return np.rot90(arr, k=-1).min(axis=1)


# def min_value_array(arr):
#     return np.array(arr).min(axis=0)


# def min_value_array(arr):
#     return np.min(arr, axis=0)


# def min_value_array(arr):
#     return [min(col) for col in zip(*arr)]


def min_value_array(arr: np.ndarray):
    return arr.min(0)


# [1, 2, 3, 4]
# [-1, 0, 4, 3]
# [0, 6, 7, -2]]

# [1, -1, 0]
# [2, 0, 6]
# [3, 4, 7]
# [4, 3, -2]
