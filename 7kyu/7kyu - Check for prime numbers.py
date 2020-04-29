# 7kyu - Check for prime numbers

""" In this kata you will create a function to check a non-negative input to see if it is a prime number.
The function will take in a number and will return True if it is a prime number and False if it is not.
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. """


# def is_prime(n):
#     return n > 1 and all(n % i for i in range(2, n))

# def is_prime(n):
#     return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))

def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5)+1, 2))


q = is_prime(0), False
q
q = is_prime(1), False
q
q = is_prime(2), True
q
q = is_prime(11), True
q
q = is_prime(12), False
q
q = is_prime(571), True
q
q = is_prime(25), False
q
