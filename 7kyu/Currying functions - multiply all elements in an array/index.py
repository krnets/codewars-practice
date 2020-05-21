# 7kyu - Currying functions: multiply all elements in an array

""" To complete this Kata you need to make a function multiply_all which takes an array of integers as an argument. 
This function must return another function, which takes a single integer as an argument and returns a new array.

The returned array should consist of each of the elements from the first array multiplied by the integer.

Example:

multiply_all([1, 2, 3])(2); // => [2, 4, 6] """


def multiply_all(arr):
    def multiply(num):
        return [num * x for x in arr]
    return multiply


# must return an array
q = isinstance(multiply_all([1])(1), list)
q

# array has correct length
q = len(multiply_all([1, 2])(1))  # 2
q

# returned array has correct values
q = multiply_all([1, 2, 3])(1)  # [1, 2, 3]
q
q = multiply_all([1, 2, 3])(2)  # [2, 4, 6]
q
q = multiply_all([1, 2, 3])(0)  # [0, 0, 0]
q
q = multiply_all([])(10)  # []
q
