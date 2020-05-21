# 7kyu - Sum of squares less than some number

""" Write a function that will return how many integer (starting from 1, 2...) numbers 
raised to power of 2 and then summed up are less than some number given as a parameter.

E.g 1: For n = 6  result should be 2 because 1^2 + 2^2 = 1 + 4 = 5 and 5 < 6 
E.g 2: For n = 15 result should be 3 because 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14 and 14 < 15 """

# def get_number_of_squares(n):
#     acc, i = 0, 0
#     while acc < n:
#         i += 1
#         acc += i ** 2
#     return i - 1

def get_number_of_squares(n):
    k = 1
    while k*(k+1)*(2*k+1)/6 < n:
        k += 1
    return k - 1


q = get_number_of_squares(1)  # 0
q
q = get_number_of_squares(2)  # 1
q
q = get_number_of_squares(5)  # 1
q
q = get_number_of_squares(6)  # 2
q
q = get_number_of_squares(15)  # 3
q
