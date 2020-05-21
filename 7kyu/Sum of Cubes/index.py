# 7kyu - Sum of Cubes

""" Write a function that takes a positive integer n, sums all the cubed values from 1 to n, and returns that sum.

Assume that the input n will always be a positive integer.

sum_cubes(2)
> 9 
# sum of the cubes of 1 and 2 is 1 + 8 """


def sum_cubes(n):
    return sum(x ** 3 for x in range(n + 1))


q = sum_cubes(1)  # 1
q
q = sum_cubes(2)  # 9
q
q = sum_cubes(3)  # 36
q
q = sum_cubes(4)  # 100
q
q = sum_cubes(10)  # 3025
q
q = sum_cubes(123)  # 58155876
q
