def diagonal(ar):
    n = len(ar)
    res = []

    for m in range(2 * n - 2, -1, -1):
        r = max(0, m - n + 1)
        c = m - r

        while r < n and c >= 0:
            res.append(ar[r][c])
            r += 1
            c -= 1

    return res
