# 7kyu - Sum - Square Even, Root Odd

""" You will be given a list of numbers, nums, as the only argument to the function. 
Take each number in the list and square it if it is even, or square root the number if it is odd. 
Take this new list and find the sum, rounding to two decimal places.

The list will never be empty and will only contain values that are greater than or equal to zero. """


# def sum_square_even_root_odd(nums):
#     return round(sum(x**0.5 if x % 2 else x*x for x in nums), 2)

def sum_square_even_root_odd(nums):
    return round(sum(n**(0.5 if n % 2 else 2) for n in nums), 2)


q = sum_square_even_root_odd([4, 5, 7, 8, 1, 2, 3, 0]), 91.61
q
q = sum_square_even_root_odd([1, 14, 9, 8, 17, 21]), 272.71
q
