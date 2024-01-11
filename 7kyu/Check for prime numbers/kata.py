from math import sqrt


def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(sqrt(n)) + 1))


# def is_prime(n):  # fast but it throws up false positives like 341l, 541, 645 etc
#     return pow(2, n - 1, n) == 1 if n > 2 else n == 2
