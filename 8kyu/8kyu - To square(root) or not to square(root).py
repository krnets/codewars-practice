# 8kyu - To square(root) or not to square(root)

""" Write a method, that will get an integer array as parameter and will process every number from this array.
Return a new array with processing every number of the input-array like this:

If the number has an integer square root, take this, otherwise square the number.

[4,3,9,7,2,1] -> [2,9,3,49,4,1]

The input array will always contain only positive numbers and will never be empty or null.

The input array should not be modified! """

# from math import sqrt

# def square_or_square_root(arr):
#     res = []
#     for x in arr:
#         temp = sqrt(x)
#         if int(temp) == temp:
#             res.append(int(temp))
#         else: res.append(x * x)
#     return res

def square_or_square_root(arr):
    res = []
    for x in arr:
        root = x ** 0.5
        if root.is_integer():
            res.append(int(root))
        else:
            res.append(x * x)
    return res

q = square_or_square_root([4, 3, 9, 7, 2, 1 ]) # [2, 9, 3, 49, 4, 1])
q
q = square_or_square_root([100, 101, 5, 5, 1, 1]) # [10, 10201, 25, 25, 1, 1])
q
q = square_or_square_root([1, 4, 9, 2, 25, 36]) # [1, 2, 3, 4, 5, 6]
q