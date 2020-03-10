# 6kyu - Find The Parity Outlier

""" You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.

[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number) """


# def find_outlier(integers):
#     odd, even = [], []
#     for x in integers:
#         if x % 2 == 0:
#             even.append(x)
#         else:
#             odd.append(x)
#     if len(odd) == 1:
#         return odd[0]
#     else:
#         return even[0]

# def find_outlier(integers):
#     odd, even = [], []
#     [odd.append(x) if x % 2 else even.append(x) for x in integers]
#     return odd[0] if len(odd) == 1 else even[0]

# def find_outlier(integers):
#     parity = [n % 2 for n in integers]
#     return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(sum(parity) == 1)]


q = find_outlier([2, 4, 6, 8, 10, 3])  # 3
q
q = find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])  # 11
q
q = find_outlier([160, 3, 1719, 19, 11, 13, -21])  # 160
q
