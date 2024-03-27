from gmpy2 import next_prime


def prime_factors(n):
    prime, res = 2, []

    while n > 1:
        while n % prime == 0:
            n //= prime
            res.append(prime)
        prime = next_prime(prime)

    return res
