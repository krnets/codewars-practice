# 6kyu - Transform To Prime

""" Given a List [] of n integers, find minimum mumber to be inserted in a list, 
so that sum of all elements of list should equal the closest prime number.

    List size is at least 2 .
    List's numbers will only positives (n > 0).
    Repeatition of numbers in the list could occur.
    The newer list's sum should equal the closest prime number.

Input >> Output Examples

1- minimumNumber ({3,1,2}) ==> return (1)
    Since, the sum of the list's elements equal to (6), the minimum number to be inserted to transform the sum to prime number is (1), 
    which will make *the sum of the List** equal the closest prime number (7)* .

2-  minimumNumber ({2,12,8,4,6}) ==> return (5)
    Since, the sum of the list's elements equal to (32), the minimum number to be inserted to transform the sum to prime number is (5), 
    which will make *the sum of the List** equal the closest prime number (37)* .

3- minimumNumber ({50,39,49,6,17,28}) ==> return (2)
    Since, the sum of the list's elements equal to (189), the minimum number to be inserted to transform the sum to prime number is (2), 
    which will make *the sum of the List** equal the closest prime number (191)* . """

# def is_prime(n):
#     return n > 1 and all(n % i for i in range(2, int(n ** .5) + 1))

def is_prime(n):
    return n == 2 or n % 2 and all(n % i for i in range(3, int(n ** .5) + 1, 2))

def next_prime(n):
    while not is_prime(n):
        n += 1
    return n

def minimum_number(numbers):
    s = sum(numbers)
    return 0 if is_prime(s) else next_prime(s) - s

# from sympy import *
# import sympy

# def minimum_number(numbers):
#     s = sum(numbers)
#     return sympy.isprime(5)

q = minimum_number([3, 1, 2])  # 1
q
q = minimum_number([5, 2])  # 0
q
q = minimum_number([1, 1, 1])  # 0
q
q = minimum_number([2, 12, 8, 4, 6])  # 5
q
q = minimum_number([50, 39, 49, 6, 17, 28])  # 2
q
