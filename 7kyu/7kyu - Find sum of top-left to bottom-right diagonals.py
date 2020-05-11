# 7kyu - Find sum of top-left to bottom-right diagonals

""" Given a square matrix (i.e. an array of subarrays), find the sum of values from the first value of the first array, 
the second value of the second array, the third value of the third array, and so on...
Examples

array = [[1, 2],
         [3, 4]]

diagonal sum: 1 + 4 = 5

array = [[5, 9, 1, 0],
         [8, 7, 2, 3],
         [1, 4, 1, 9],
         [2, 3, 8, 2]]

diagonal sum: 5 + 7 + 1 + 2 = 15 """


# def diagonal_sum(array):
#     res = []
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             if i == j:
#                 res.append(int(array[i][j]))
#     return res

# def diagonal_sum(array):
#     return sum(array[i][j] for i in range(len(array)) for j in range(len(array[i])) if i == j)

# def diagonal_sum(array):
#     return sum(array[i][i] for i in range(len(array)))

# def diagonal_sum(array):
#     return sum(row[i] for i, row in enumerate(array))

from numpy import trace as diagonal_sum


q = diagonal_sum([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]), 15
q

q = diagonal_sum([
    [1, 2],
    [3, 4]]), 5
q

q = diagonal_sum([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]), 34
q
