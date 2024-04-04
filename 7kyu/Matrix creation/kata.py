# def get_matrix(n):
#     matrix = []
#     for i in range(n):
#         row = [0] * n
#         row[i] = 1
#         matrix.append(row)
#     return matrix

# import numpy as np

# def get_matrix(n):
#     return np.identity(n).tolist()


def get_matrix(n):
    return [[(0, 1)[i == j] for j in range(n)] for i in range(n)]
