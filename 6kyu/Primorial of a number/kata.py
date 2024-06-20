from gmpy2 import next_prime


def num_primorial(n):
    x, res = 1, 1
    for _ in range(n):
        x = next_prime(x)
        res *= x
    return res
