def sum_arrays(arrays, shift):
    m, n = len(arrays), len(arrays[0])
    res = [0] * (shift * (m - 1) + n)

    for i in range(m):
        for j in range(n):
            res[i * shift + j] += arrays[i][j]

    return res
