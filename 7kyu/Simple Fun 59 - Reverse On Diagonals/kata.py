# def reverse_on_diagonals(matrix):
#     n = len(matrix)
#     for i in range(n // 2):
#         j = -(i + 1)
#         matrix[i][i], matrix[j][j], matrix[j][i], matrix[i][j] = (
#             matrix[j][j],
#             matrix[i][i],
#             matrix[i][j],
#             matrix[j][i],
#         )
#     return matrix


def reverse_on_diagonals(matrix):
    n = len(matrix)
    for i in range(n // 2):
        j = -(i + 1)
        matrix[i][i], matrix[j][j] = matrix[j][j], matrix[i][i]
        matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    return matrix
