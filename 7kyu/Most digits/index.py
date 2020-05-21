# 7kyu - Most digits

""" Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array. """


# def find_longest(arr):
#     res = [len(str(x)) for x in arr]
#     return arr[res.index(max(res))]

def find_longest(arr):
    return max(arr, key=lambda x: len(str(x)))


q = find_longest([1, 10, 100]), 100
q
q = find_longest([9000, 8, 800]), 9000
q
q = find_longest([8, 900, 500]), 900
q
q = find_longest([3, 40000, 100]), 40000
q
q = find_longest([1, 200, 100000]), 100000
q
