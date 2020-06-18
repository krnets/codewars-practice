""" 7kyu - Excessively Abundant Numbers

An abundant number or excessive number is a number for which the sum of its proper divisors is greater than the number itself.
The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16 (> 12).
Derive function abundant_number(num) which returns true if num is abundant, false if not. """

# def abundant_number(num):
#     sum = 0
#     for i in range(1, num//2+1):
#         if num % i == 0:
#             sum += i
#     return sum > num


def abundant_number(num):
    return sum(i for i in range(1, num//2 + 1) if num % i == 0) > num


q = abundant_number(12), True
q
q = abundant_number(18), True
q
q = abundant_number(37), False
q
q = abundant_number(120), True
q
q = abundant_number(77), False
q
