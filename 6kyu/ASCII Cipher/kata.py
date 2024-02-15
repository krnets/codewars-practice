from gmpy2 import is_prime


def ascii_cipher(message, key):
    sign = (1, -1)[key < 0]
    larget_prime = max(get_prime_factors(abs(key))) * sign
    return "".join(chr((ord(c) + larget_prime) % 128) for c in message)


def get_prime_factors(n):
    return [i for i in range(2, n + 1) if n % i == 0 and is_prime(i)]
