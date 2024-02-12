# def f(n):
#     return 1 if n == 0 else n - m(f(n - 1))


# def m(n):
#     return 0 if n == 0 else n - f(m(n - 1))

from functools import lru_cache


@lru_cache
def f(n):
    return n - m(f(n - 1)) if n else 1


@lru_cache
def m(n):
    return n - f(m(n - 1)) if n else 0
