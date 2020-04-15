# 6kyu - Calculate the function f(x) for a simple linear sequence (Medium)

""" This time, for any given linear sequence, calculate the function [f(x)] and 
return it as a function in Javascript or Lambda/Block in Ruby.

get_function([0, 1, 2, 3, 4])(5) => 5
get_function([0, 3, 6, 9, 12])(10) => 30
get_function([1, 4, 7, 10, 13])(20) => 61

Assumptions for this kata are:

The sequence argument will always contain 5 values equal to f(0) - f(4).
The function will always be in the format "nx +/- m", 'x +/- m', 'nx', 'x' or 'm'
If a non-linear sequence simply return 'Non-linear sequence' """

# def get_function(sequence):
#     m = sequence[0]
#     n = sequence[1] - m
#     if any(s != n*i+m for i, s in enumerate(sequence)):
#         return "Non-linear sequence"
#     return lambda x: n * x + sequence[0]

def get_function(sequence):
    if len(set(y - x for x, y in zip(sequence, sequence[1:]))) != 1:
        return 'Non-linear sequence'
    return lambda x: (sequence[2] - sequence[1]) * x + sequence[0]


q = get_function([0, 1, 2, 3, 4])(5)  # 5
q
q = get_function([0, 3, 6, 9, 12])(10)  # 30
q
q = get_function([1, 4, 7, 10, 13])(20)  # 61
q
q = get_function([1, 4, 7, 10, 12])(20)  # 61
q
