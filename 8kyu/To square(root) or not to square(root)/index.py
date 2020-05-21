# 8kyu - To square(root) or not to square(root)

""" Write a method, that will get an integer array as parameter and will process every number from this array.
Return a new array with processing every number of the input-array like this:

If the number has an integer square root, take this, otherwise square the number.

[4,3,9,7,2,1] -> [2,9,3,49,4,1]

The input array will always contain only positive numbers and will never be empty or null.
The input array should not be modified! """


# def square_or_square_root(arr):
#     res = []
#     for x in range(len(arr)):
#         tmp = x ** 0.5
#         if round(tmp) == tmp:
#             res.append(int(tmp))
#         else:
#             res.append(x * x)
#     return res


def square_or_square_root(arr):
    return [int(x**0.5) if round(x**0.5) == x**0.5 else x*x for x in arr]


q = square_or_square_root([4, 3, 9, 7, 2, 1]), [2, 9, 3, 49, 4, 1]
q
q = square_or_square_root([100, 101, 5, 5, 1, 1]), [10, 10201, 25, 25, 1, 1]
q
q = square_or_square_root([1, 2, 3, 4, 5, 6]), [1, 4, 9, 2, 25, 36]
q
