""" 6kyu - Backwards Read Primes

Backwards Read Primes are primes that when read backwards in base 10 (from right to left) are a different prime.
(This rules out primes which are palindromes.)

Examples:
13 17 31 37 71 73 are Backwards Read Primes

13 is such because it's prime and read from right to left writes 31 which is prime too. Same for the others.

Find all Backwards Read Primes between two positive given numbers (both inclusive),
the second one always being greater than or equal to the first one.
The resulting array or the resulting string will be ordered following the natural order of the prime numbers.

Return only the first backwards-read prime between start and end or 0 if you don't find any """

# def is_prime(n):
#     return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))

# def is_prime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return n > 1

# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     return n % 2 and all(n % i for i in range(3, int(n**0.5)+1, 2))


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return all(n % i != 0 for i in range(3, int(n**0.5)+1, 2))


def is_backwards_read_prime(n):
    return is_prime(int(str(n)[::-1]))


def is_palindrome(n):
    return n == int(''.join(str(n)[::-1]))


def backwards_prime(start, stop):
    return [i for i in range(start, stop+1) if is_prime(i) and is_backwards_read_prime(i) and not is_palindrome(i)]


q = backwards_prime(7000, 7100)  # [7027, 7043, 7057]
q
q = backwards_prime(400, 503)  # []
q
q = backwards_prime(501, 599)  # []
q
q = backwards_prime(2, 100)  # [13, 17, 31, 37, 71, 73, 79, 97]
q
q = backwards_prime(9900, 10000)  # [9923, 9931, 9941, 9967]
q
