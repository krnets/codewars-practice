def rotate_corners(matrix):
    a = matrix[0][0]
    b = matrix[0][-1]
    c = matrix[-1][-1]
    d = matrix[-1][0]

    f = lambda x: ord(x) if isinstance(x, str) else x
    sum_corners = sum(map(f, [a, b, c, d]))
    sum_matrix = sum(sum(map(f, row)) for row in matrix)

    n = 4 - (sum_matrix - sum_corners) * sum_corners % 4
    for _ in range(n):
        a, b, c, d = b, c, d, a
    return [[a, b], [d, c]]
