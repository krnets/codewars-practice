def fibonacci(n):
    if n < 0:
        return []
    res, a, b = [], 0, 1
    while len(res) < n:
        res.append(a)
        a, b = b, a + b
    return res
