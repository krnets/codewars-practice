# 6kyu - Compare powers

""" You certainly can tell which is the larger number between 210 and 215.

But what about, say, 210 and 310? You know this one too.

Things tend to get a bit more complicated with both different bases and exponents: 
which is larger between 39 and 56?

Well, by now you have surely guessed that you have to build a function to compare powers, returning -1 if the 
first member is larger, 0 if they are equal, 1 otherwise; 

Powers to compare will be provided in the [base, exponent] format:

compare_powers([2,10],[2,15])==1
compare_powers([2,10],[3,10])==1
compare_powers([2,10],[2,10])==0
compare_powers([3,9],[5,6])==-1
compare_powers([7,7],[5,8])==-1

Only positive integers will be tested, incluing bigger numbers - you are warned now, so be diligent 
try to implement an efficient solution. """

# import math

# def compare_powers(n1, n2):
#     a = math.log10(n1[0]) * n1[1]
#     b = math.log10(n2[0]) * n2[1]
#     return -1 if a > b else 1 if a < b else 0

# def compare_powers(n1, n2):
#     a = math.log(n1[0]) * n1[1]
#     b = math.log(n2[0]) * n2[1]
#     return -1 if a > b else 1 if a < b else 0

# from math import log


# def compare_powers(n1, n2):
#     a = log(n1[0]) * n1[1]
#     b = log(n2[0]) * n2[1]
#     return -1 if a > b else 1 if a < b else 0

# def compare_powers(*nums):
#     a, b = map(lambda x: log(x[0]) * x[1], nums)
#     return (a < b) - (a > b)

import math

def compare_powers(*args):
    a, b = map(lambda x: math.log(x[0]) * x[1], args)
    return (a < b) - (a > b)


q = compare_powers([2, 10], [2, 15])  # 1
q
q = compare_powers([2, 10], [3, 10])  # 1
q
q = compare_powers([2, 10], [2, 10])  # 0
q
q = compare_powers([3, 9], [5, 6])  # -1
q
q = compare_powers([7, 7], [5, 8])  # -1
q
