# 5kyu - Primes with Even Digits

""" Find the closest prime number under a certain integer n 
that has the maximum possible amount of even digits.

For n = 1000, the highest prime under 1000 is 887, having two even digits (8 twice)

Naming f(), the function that gives that prime, the above case and others will be like the following below.

f(1000) ---> 887 (even digits: 8, 8)
f(1210) ---> 1201 (even digits: 2, 0)
f(10000) ---> 8887
f(500) ---> 487
f(487) ---> 467

Features of the random tests:

Number of tests = 28
1000 <= n <= 5000000 """

# def is_prime(n):
#     return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))

# def is_prime(n):
#     if n < 2:
#         return False
#     elif n == 2:
#         return True
#     elif n % 2 == 0:
#         return False
#     for i in range(3, int(n ** 0.5)+1, 2):
#         if n % i == 0:
#             return False
#     return True

# def f(n):
#     result, max_evens = 0, 0
#     for x in range(n-1, 1, -1):
#         if len(str(x))-1 <= max_evens:
#             return result
#         n_evens = sum(d in '02468' for d in str(x))
#         if n_evens > 1 and is_prime(x):
#             if n_evens > max_evens:
#                 result = x
#                 max_evens = n_evens

def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def f(n):
    max_prime, max_evens = 0, 0
    for x in range(n-1, 1, -1):
        if len(str(x)) <= max_evens+1:
            return max_prime
        n_evens = sum(d in '02468' for d in str(x))
        if n_evens > 1 and is_prime(x):
            if n_evens > max_evens:
                max_evens = n_evens
                max_prime = x


q = f(1000), 887
q
q = f(1210), 1201
q
q = f(10000), 8887
q
q = f(500), 487
q
q = f(487), 467
q
q = f(1523), 1489
q
q = f(953), 887
q
q = f(3751), 2887
q
