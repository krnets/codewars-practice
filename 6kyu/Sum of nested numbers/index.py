# 6kyu - Sum of nested numbers

""" Build a function sumNestedNumbers/sum_nested_numbers that finds the sum of all numbers 
in a series of nested arrays raised to the power of their respective nesting levels. 
Numbers in the outer most array should be raised to the power of 1.

For example,

sumNestedNumbers([1, [2], 3, [4, [5]]])

should return 1 + 2*2 + 3 + 4*4 + 5*5*5 === 149 """


def sum_nested_numbers(arr, depth=1):
    return sum(sum_nested_numbers(a, depth+1) if isinstance(a, list) else pow(a, depth) for a in arr)


q = sum_nested_numbers([1, 2, 3, 4, 5])  # 15
q
q = sum_nested_numbers([1, [2], 3, [4, [5]]])  # 149
q
q = sum_nested_numbers([6, [5], [[4]], [[[3]]], [[[[2]]]], [[[[[1]]]]]])  # 209
q
q = sum_nested_numbers([1, [-1], [[1]], [[[-1]]], [[[[1]]]]])  # 5
q
