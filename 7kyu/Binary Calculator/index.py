# 7kyu - Binary Calculator

""" In this kata you need to write a function that will receive two strings (n1 and n2), 
each representing an integer as a binary number. A third parameter will be provided (o) 
as a string representing one of the following operators: add, subtract, multiply.

Your task is to write the calculate function so that it will perform the arithmetic and 
the result returned should be a string representing the binary result.

Examples:

1 + 1 === 10
10 + 10 === 100

Negative binary numbers are usually preceded by several 1's. 
For this kata, negative numbers can be represented with the negative symbol at the beginning of the string.

Examples of negatives:

1 - 10 === -1
10 - 100 === -10 """


# def calculate(n1, n2, op):
#     n1, n2 = int(n1, 2), int(n2, 2)

#     res = {'subtract': lambda x, y: x - y,
#            'multiply': lambda x, y: x * y,
#            'add': lambda x, y: x + y,
#            }[op](n1, n2)

#     return f'{res:b}'

from operator import *

def calculate(n1, n2, op):
    return f'{eval(op[:3])(int(n1, 2), int(n2, 2)):b}'


q = calculate('1', '1', 'add'), '10'
q
q = calculate('1', '1', 'subtract'), '0'
q
q = calculate('1', '1', 'multiply'), '1'
q
q = calculate('1010100111', '1000101001', 'subtract')
q
#     '1111110'
q = calculate('111110', '10001111', 'subtract')
q
#      -1010001'
