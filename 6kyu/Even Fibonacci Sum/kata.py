def even_fib(n):
    res, a, b = 0, 0, 1
    while a < n:
        if a % 2 == 0:
            res += a
        a, b = b, a + b
    return res