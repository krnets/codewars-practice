# 6kyu - Is a number prime?

""" Define a function that takes an integer argument and returns logical value true or false 
depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has 
no positive divisors other than 1 and itself.

is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */

Assumptions

    You can assume you will be given an integer input.
    You can not assume that the integer will be only positive. 
    You may be given negative numbers as well (or 0).
    There are no fancy optimizations required, but still the most trivial solutions might time out. 
    Try to find a solution which does not loop all the way up to n. """


# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return num >= 2

def is_prime(num):
    return num > 1 and all(num % d for d in range(2, int(num**0.5)+1))


q = is_prime(0)  # False
q
q = is_prime(1)  # False
q
q = is_prime(2)  # True
q
q = is_prime(73)  # True
q
q = is_prime(75)  # False
q
q = is_prime(3)  # True
q
q = is_prime(5)  # True
q
q = is_prime(7)  # True
q
q = is_prime(41)  # True
q
q = is_prime(5099)  # True
q
q = is_prime(4)  # False
q
q = is_prime(6)  # False
q
q = is_prime(8)  # False
q
q = is_prime(9)  # False
q
q = is_prime(45)  # False
q
q = is_prime(-1)  # False
q
q = is_prime(-5)  # False
q
q = is_prime(-8)  # False
q
q = is_prime(-41)  # False
q
