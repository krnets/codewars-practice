# 7kyu - Simple Maths Test

""" Create a function which checks a number for three different properties.

    is the number prime?
    is the number even?
    is the number a multiple of 10?

Each should return either true or false, which should be given as an array. Remark: The Haskell variant uses data Property.

number_property(7)  # ==> [true,  false, false] 
number_property(10) # ==> [false, true,  true] 

The number will always be an integer, either positive or negative. Note that negative numbers cannot be primes, but they can be multiples of 10:

number_property(-7)  # ==> [false, false, false] 
number_property(-10) # ==> [false, true,  true]  """


# import sympy

# def number_property(n):
#     return [sympy.isprime(n), n % 2 == 0, n % 10 == 0]

def is_prime(num):
    return num > 1 and all(num % d for d in range(2, int(num**0.5)+1))

def number_property(n):
    return [is_prime(n), n % 2 == 0, n % 10 == 0]


q = number_property(-10), [False, True, True]
q
q = number_property(2), [True, True, False]
q
q = number_property(120), [False, True, True]
q
q = number_property(125), [False, False, False]
q
