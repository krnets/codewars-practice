""" 7kyu - This is odd

Create a function that checks if a number is odd.
Expect negative and decimal numbers too. 
Remember... all negative numbers can also be either odd or even.

Decimal numbers always return false

is_odd(2)--> false
is_odd(5)--> true
is_odd(4)--> false
is_odd(-17)--> true
is_odd(-7.0)--> true
is_odd(-7.1)--> false
is_odd(4.23)--> false
is_odd(5.0)--> true
is_odd(5.23)--> false """

# def is_odd(n):
#     return isinstance(n, (int, float)) and int(n) == n and n % 2 != 0

# def is_odd(n):
#     return n % 2 == 1


def is_odd(n):
    return n == int(n) and n % 2 != 0


q = is_odd(-1.7265), False
q
q = is_odd(-277.8333333333333), False
q
q = is_odd(5), True
q
q = is_odd(4), False
q
q = is_odd(3), True
q
q = is_odd(1), True
q
q = is_odd(0), False
q
q = is_odd(-5), True
q
q = is_odd(-4), False
q
q = is_odd(3.0), True
q
q = is_odd(-0.1), False
q
q = is_odd(0.25), False
q
