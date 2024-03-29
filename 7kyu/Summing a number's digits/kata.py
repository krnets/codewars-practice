# 7kyu - Summing a number's digits

""" Write a function named sumDigits which takes a number as input and 
returns the sum of the absolute value of each of the number's decimal digits. 

  sum_digits(10)  # Returns 1
  sum_digits(99)  # Returns 18
  sum_digits(-32) # Returns 5

Let's assume that all numbers in the input will be integer values. """


# def sum_digits(number):
#     return sum(int(x) for x in str(abs(number)))

# def sum_digits(number):
#     number = abs(number)
#     sum = 0

#     while number != 0:
#         sum += number % 10
#         number //= 10

#     return sum


def sum_digits(number):
    return sum(map(int, str(abs(number))))


q = sum_digits(10)  # 1
q
q = sum_digits(99)  # 18
q
q = sum_digits(-32)  # 5
q
