# 8kyu - Can we divide it?

""" Your task is to create functionis is_divide_by to check if an integer number is divisible by each out of two arguments.

A few cases:


(-12, 2, -6)  ->  true
(-12, 2, -5)  ->  false

(45, 1, 6)    ->  false
(45, 5, 15)   ->  true

(4, 1, 4)     ->  true
(15, -5, 3)   ->  true """


def is_divide_by(number, a, b):
    return number % a == 0 and number % b == 0


q = is_divide_by(-12, 2, -6)  # True
q
q = is_divide_by(-12, 2, -5)  # False
q
q = is_divide_by(45, 1, 6)  # False
q
q = is_divide_by(45, 5, 15)  # True
q
q = is_divide_by(4, 1, 4)  # True
q
q = is_divide_by(15, -5, 3)  # True
q
