""" 7kyu - Sexy Primes <3

Sexy primes are pairs of two primes that are 6 apart. 
In this kata, your job is to complete the function sexy_prime(x, y) which returns true if x & y are sexy, false otherwise.

Examples:

sexy_prime(5,11)
--> True

sexy_prime(61,67)
--> True

sexy_prime(7,13)
--> True

sexy_prime(5,7)
--> False

sexy_prime(1,7)
--> False
( 1 is not considered prime )

Note: x & y are always positive integers > 0, but they are not always in order of precendence...
you can be given either (5,11) or (11,5). Both are equally valid. """


def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))

def sexy_prime(x, y):
    return abs(x - y) == 6 and is_prime(x) and is_prime(y)


q = sexy_prime(5, 11), True
q
q = sexy_prime(13, 19), True
q
q = sexy_prime(83, 89), True
q
q = sexy_prime(1, 11), False
q
