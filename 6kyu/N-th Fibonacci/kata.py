from gmpy2 import fib

# def nth_fib(n):
#     return int(fib(n - 1))


# def nth_fib(n):
#     if n < 2:
#         return 0
#     a, b = 1, 1
#     for _ in range(n - 2):
#         a, b = b, a + b
#     return a


def nth_fib(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a
