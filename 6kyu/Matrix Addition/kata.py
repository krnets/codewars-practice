# import numpy as np

# def matrix_addition(a, b):
# return np.ma.add(a, b).tolist()
# return np.add(a, b).tolist()


def matrix_addition(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            c[row][col] = a[row][col] + b[row][col]
    return c
