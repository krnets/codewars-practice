# 7kyu - Form The Minimum

""" Given a list of digits, return the smallest number that could be formed from these digits, 
using the digits only once (ignore duplicates).

    Only positive integers will be passed to the function (> 0 ), no negatives or zeros.

Input >> Output Examples

minValue ({1, 3, 1})  ==> return (13)
    (13) is the minimum number could be formed from {1, 3, 1} , Without duplications

minValue({5, 7, 5, 9, 7})  ==> return (579)
    (579) is the minimum number could be formed from {5, 7, 5, 9, 7} , Without duplications

minValue({1, 9, 3, 1, 7, 4, 6, 6, 7}) return  ==> (134679)
    (134679) is the minimum number could be formed from {1, 9, 3, 1, 7, 4, 6, 6, 7} , Without duplications  """


def min_value(digits):
    return int(''.join(map(str, sorted(set(digits)))))

# from functools import reduce

# def min_value(digits):
#     return reduce(lambda a, b: a * 10 + b, sorted(set(digits)))


q = min_value([1, 3, 1])  # 13
q
q = min_value([4, 7, 5, 7])  # 457
q
q = min_value([4, 8, 1, 4])  # 148
q
