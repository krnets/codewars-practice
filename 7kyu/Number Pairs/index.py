# 7kyu - Number Pairs

""" In this Kata the aim is to compare each pair of integers from 2 arrays, and return a new array of large numbers.
Both arrays have the same dimensions.

arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
get_larger_numbers(arr1, arr2) == [23, 64, 53, 17, 88] """


# def get_larger_numbers(a, b):
#     return [max(x, y) for x, y, in zip(a, b)]

# def get_larger_numbers(a, b):
#     return list(map(max, a, b))

def get_larger_numbers(a, b):
    return [max(pair) for pair in zip(a, b)]


a = [13, 64, 15, 17, 88]
b = [23, 14, 53, 17, 80]

q = get_larger_numbers(a, b)
q
#      [23, 64, 53, 17, 88]

a = [34, -64, 15, 17, 88]
b = [23, 14, 53, 17, 80]

q = get_larger_numbers(a, b)
q
#      [34, 14, 53, 17, 88]
