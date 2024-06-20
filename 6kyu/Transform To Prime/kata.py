from gmpy2 import next_prime, is_prime

# def minimum_number(numbers):
#     n = sum(numbers)
#     return 0 if is_prime(n) else next_prime(n) - n


def minimum_number(numbers):
    return 0 if is_prime(n := sum(numbers)) else next_prime(n) - n
