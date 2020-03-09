# 7kyu - Product Array (Array Series #5)

""" Given an array/list [] of integers , Construct a product array Of same size
    such shat prod[i] is equal to The Product of all the elements of Arr[] except Arr[i].
    Array/list size is at least 2 .
    Array/list's numbers Will be only Positives
    Repetition of numbers in the array/list could occur.

Input >> Output Examples

productArray ({12,20}) ==>  return {20,12}
    The first element in prod [] array 12 is the product of all array's elements except the first element
    The second element 20 is the product of all array's elements except the second element .

productArray ({1,5,2}) ==> return {10,2,5}
    The first element 10 is the product of all array's elements except the first element *1***
    The second element 2 is the product of all array's elements except the second element 5
    The Third element 5 is the product of all array's elements except the Third element 2.

productArray ({10,3,5,6,2}) return ==> {180,600,360,300,900}
    The first element 180 is the product of all array's elements except the first element 10
    The second element 600 is the product of all array's elements except the second element 3
    The Third element 360 is the product of all array's elements except the third element 5
    The Fourth element 300 is the product of all array's elements except the fourth element 6
    Finally ,The Fifth element 900 is the product of all array's elements except the fifth element 2 """

# 01234
# 0 1234
# 01 234
# 012 34
# 0123 4
# 01234

# def product_array(numbers):
#     res = [reduce(mul, numbers[1:])]
#     for i in range(len(numbers) - 1):
#         temp = numbers[:i+1]
#         temp += numbers[i+2:]
#         res.append(reduce(mul, temp))
#     return res


# from operator import mul
# from functools import reduce

# def product_array(numbers):
#     tot = reduce(mul, numbers)
# return [tot // n for n in numbers]


from numpy import prod

def product_array(numbers):
    p = prod(numbers)
    return [p // n for n in numbers]


q = product_array([12, 20])  # [20,12]
q
q = product_array([12, 20])  # [20,12]
q
q = product_array([3, 27, 4, 2])  # [216,24,162,324]
q
q = product_array([13, 10, 5, 2, 9])  # [900,1170,2340,5850,1300]
q
q = product_array([16, 17, 4, 3, 5, 2])  # [2040,1920,8160,10880,6528,16320]
q
