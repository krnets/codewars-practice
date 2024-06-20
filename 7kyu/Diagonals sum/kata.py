# def sum_diagonals(matrix):
#     ans = 0
#     try:
#         for i in range(n := len(matrix)):
#             ans += matrix[i][i] + matrix[i][n - i - 1]
#         return ans
#     except:
#         return ans


def sum_diagonals(matrix):
    try:
        return sum(
            matrix[i][i] + matrix[i][len(matrix) - i - 1] for i in range(len(matrix))
        )
    except:
        return 0
