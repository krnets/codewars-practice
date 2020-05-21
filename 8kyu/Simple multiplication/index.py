# 8kyu - Simple multiplication

""" This kata is about multiplying a given number by eight if it is an even number and by nine otherwise. """


# def simple_multiplication(number):
#     return 8 * number if number % 2 == 0 else 9 * number

# def simple_multiplication(number):
#     return number * (8 if number % 2 == 0 else 9)

# def simple_multiplication(number):
#     return number * [8, 9][number % 2]

def simple_multiplication(number):
    return number * (8 + number % 2)


q = simple_multiplication(2)  # 16
q
q = simple_multiplication(1)  # 9
q
q = simple_multiplication(8)  # 64
q
q = simple_multiplication(4)  # 32
q
q = simple_multiplication(5)  # 45
q
