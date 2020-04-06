# Beta - Find the Digit Sum of the LCM

""" In this exercise, you will build a program that takes two numbers, a and b, 
and returns the digit sum of their LCM (Lowest Common Multiple). 
If the digit sum remains over 9, you must take the digit sum of that as well. 
However, the numbers will never be big enough where you need to do it more than twice.

The parameters passed will only be positive integers above 0.

For example, if the given parameters are 7 and 12, the LCM of them is 84, 
and the digit sum of 84 is 12 -> 3. So, the function should return 3. """


# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

# def digit_sum(n):
#     s = str(n)
#     while len(s) > 1:
#         s = str(sum(int(x) for x in list(s)))
#     return int(s)

# def lcm(a, b):
#     if b == 0:
#         return a
#     return digit_sum(a * b // gcd(a, b))

from fractions import gcd

def lcm(a, b):
    n = a * b // gcd(a, b)
    return n % 9 or n and 9


q = lcm(7, 12)  # 3
q
q = lcm(2, 5)  # 1
q
q = lcm(3, 6)  # 6
q
