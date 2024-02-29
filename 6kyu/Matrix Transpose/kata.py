# def transpose(matrix):
#     return [*map(list, zip(*matrix))]

# import numpy as np


# def transpose(matrix):
#     return np.transpose(matrix).tolist()


def transpose(matrix):
    res = []
    m, n = len(matrix), len(matrix[0])

    for j in range(n):
        new_row = []
        for i in range(m):
            new_row.append(matrix[i][j])
        res.append(new_row)

    return res
