# 8kyu - Find numbers which are divisible by given number

""" Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. 
First argument is an array of numbers and the second is the divisor.
Example

divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6] """


# def divisible_by(numbers, divisor):
#     return list(filter(lambda x: x % divisor == 0, numbers))

def divisible_by(numbers, divisor):
    return [x for x in numbers if x % divisor == 0]


q = divisible_by([1, 2, 3, 4, 5, 6], 2)  # [2,4,6]
q
q = divisible_by([1, 2, 3, 4, 5, 6], 3)  # [3,6]
q
q = divisible_by([0, 1, 2, 3, 4, 5, 6], 4)  # [0,4]
q
q = divisible_by([0], 4)  # [0]
q
q = divisible_by([1, 3, 5], 2)  # []
q
