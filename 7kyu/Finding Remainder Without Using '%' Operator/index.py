# 7kyu - Finding Remainder Without Using '%' Operator

""" Write a method remainder which takes two integer arguments, dividend and divisor, 
and returns the remainder when dividend is divided by divisor. 
Do NOT use the modulus operator (%) to calculate the remainder!

Dividend will always be greater than or equal to divisor.

Make sure that the implemented remainder function works exactly the same as the Modulus operator (%). """


# def remainder(dividend, divisor):
#     while dividend > 0:
#         temp = dividend - divisor
#         if temp < 0:
#             return dividend
#         dividend = temp
#     return dividend

# def remainder(dividend, divisor):
#     while dividend >= divisor:
#         dividend -= divisor
#     return dividend

def remainder(dividend, divisor):
    return float('nan') if divisor == 0 else dividend - (dividend // divisor) * divisor


q = remainder(3, 2), 1
q
q = remainder(19, 2), 1
q
q = remainder(10, 2), 0
q
q = remainder(34, 7), 6
q
q = remainder(27, 5), 2
q
