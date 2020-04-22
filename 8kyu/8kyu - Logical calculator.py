# 8kyu - Logical calculator

""" Your task is to calculate logical value of boolean array. 
Test arrays are one-dimensional and their size is in the range 1-50.

Links referring to logical operations: AND, OR and XOR.

You should begin at the first value, and repeatedly apply the logical operation 
across the remaining elements in the array sequentially.

Input: true, true, false, operator: AND
Steps: true AND true -> true, true AND false -> false
Output: false

Input: true, true, false, operator: OR
Steps: true OR true -> true, true OR false -> true
Output: true

Input: true, true, false, operator: XOR
Steps: true XOR true -> false, false XOR false -> false
Output: false

Input: boolean array, string with operator' s name: 'AND', 'OR', 'XOR'.
Output: calculated boolean """

from functools import reduce

def logical_calc(array, op):
    OPS = {'AND': 'and', 'OR': 'or', 'XOR': '^'}
    return reduce(lambda x, y: eval(f'{str(x)} {OPS[op]} {str(y)}'), array)

# from functools import reduce

# OPS = {'AND': lambda x, y: x and y,
#        'OR':  lambda x, y: x or y,
#        'XOR': lambda x, y: x ^ y}

# def logical_calc(array, op):
#     return reduce(OPS[op], array)

# from functools import reduce
# from operator import and_, or_, xor

# OPS = {'AND': and_, 'OR': or_, 'XOR': xor}

# def logical_calc(array, op):
#     return reduce(OPS[op], array)


# def logical_calc(array, op):
#     res = array[0]
#     for x in array[1:]:
#         if op == 'AND':
#             res &= x
#         elif op == 'OR':
#             res |= x
#         else:
#             res ^= x
#     return res


q = logical_calc([True, False], "AND"), False
q
q = logical_calc([True, False], "OR"), True
q
q = logical_calc([True, False], "XOR"), True
q
q = logical_calc([True, True, False], "AND"), False
q
q = logical_calc([True, True, False], "OR"), True
q
q = logical_calc([True, True, False], "XOR"), False
q
