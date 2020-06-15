""" 7kyu - Grains

Write a program that calculates the number of grains of wheat on a chessboard 
given that the number on each square is double the previous one.

There are 64 squares on a chessboard.

#Example: square(1) = 1 square(2) = 2 square(3) = 4 square(4) = 8 etc...

Write a program that shows how many grains were on each square """


# def square(number):
#     return 2**(number-1)

def square(number):
    return 1 << number-1


q = square(1), 1
q
q = square(3), 4
q
q = square(4), 8
q
q = square(16), 32768
q
q = square(32), 2147483648
q
