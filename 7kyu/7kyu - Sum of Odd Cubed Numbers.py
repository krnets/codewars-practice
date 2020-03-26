# 7kyu - Sum of Odd Cubed Numbers

""" Find the sum of the odd numbers within an array, after cubing the initial integers. 
The function should return None if any of the values aren't numbers.

Note: Booleans should not be considered as numbers. """


def cube_odd(arr):
    if all(type(x) == int for x in arr):
        return sum(x ** 3 for x in arr if x % 2)



q = cube_odd([1, 2, 3, 4])  # 28
q
q = cube_odd([-3, -2, 2, 3])  # 0
q
q = cube_odd(["a", 12, 9, "z", 42])  # None
q
q = cube_odd([1, 1])
q
