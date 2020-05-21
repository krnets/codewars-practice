# 7kyu - Sum of differences between products and LCMs

""" In this kata you need to create a function that takes a 2D array/list of non-negative integer pairs 
and returns the sum of all the "saving" that you can have getting the LCM of each couple of number 
compared to their simple product.

For example, if you are given:
[[15,18], [4,5], [12,60]]

Their product would be:
[270, 20, 720]

While their respective LCM would be:
[90, 20, 60]

Thus the result should be:
(270-90)+(20-20)+(720-60)==840
"""

# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     if b == 0:
#         return a
#     return a * b / gcd(a, b)

# def sum_differences_between_products_and_LCMs(pairs):
#     diff_sum = 0
#     products = [x[0] * x[1] for x in pairs]
#     lcms = [lcm(x[0], x[1]) for x in pairs]
#     for i in range(len(pairs)):
#         diff_sum += products[i] - lcms[i]
#     return diff_sum

from fractions import gcd

def sum_differences_between_products_and_LCMs(pairs):
    return sum(a * b - a * b // gcd(a, b) for a, b in pairs if a and b)

q = sum_differences_between_products_and_LCMs([[15,18], [4,5], [12,60]]) # 840
q
q = sum_differences_between_products_and_LCMs([[1,1], [0,0], [13,91]]) # 1092
q
q = sum_differences_between_products_and_LCMs([[15,7], [4,5], [19,60]]) # 0
q
q = sum_differences_between_products_and_LCMs([[20,50], [10,10], [50,20]]) # 1890
q
q = sum_differences_between_products_and_LCMs([]) # 0
q
