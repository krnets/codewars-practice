# 7kyu - Factorial

""" In mathematics, the factorial of a non-negative integer n, denoted by n!, 
is the product of all positive integers less than or equal to n. 
For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. 
By convention the value of 0! is 1.

Write a function to calculate factorial for a given input. 
If input is below 0 or above 12 throw an exception of type ValueError (Python) or return -1 (C). """

# def factorial(n):
#     if n < 0 or n > 12:
#         raise ValueError
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    return 1 if n <= 1 else n * factorial(n - 1)

# def factorial(n):
#     if 0 <= n <= 12:
#         return 1 if n <= 1 else n * factorial(n - 1)
#     raise ValueError


q = factorial(0)  # 1
q
q = factorial(1)  # 1
q
q = factorial(2)  # 2
q
q = factorial(3)  # 6
q
# q = factorial(-3)  # 6
# q
