from functools import reduce
from math import prod
from operator import mul
import numpy as np


def main_diagonal_product(mat):
    return np.ma.prod(np.ma.diag(mat), dtype=object)


# def main_diagonal_product(mat):
#     return np.array(np.diagonal(mat)).prod()


# def main_diagonal_product(mat):
#     return reduce(mul, (mat[i][i] for i in range(len(mat))))


# def main_diagonal_product(mat):
#     return prod(mat[i][i] for i in range(len(mat)))
