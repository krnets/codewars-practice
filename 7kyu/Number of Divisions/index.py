# 7kyu - Number of Divisions

""" Calculate how many times a number can be divided by a given number.

For example the number 6 can be divided by 2 two times:

1. 6 / 2 = 3
2. 3 / 2 = 1 remainder = 1

100 can be divided by 2 six times:

1. 100 / 2 = 50
2. 50 / 2 = 25
3. 25 / 2 = 12 remainder 1
4. 12 / 2 = 6
5. 6 / 2 = 3
6. 3 / 2 = 1 remainder 1 """


# def divisions(n, divisor):
#     count = 0
#     while n > 0:
#         n = n // divisor
#         count += 1
#     return count - 1

# def divisions(n, divisor):
#     count = 0
#     while n >= divisor:
#         n = n // divisor
#         count += 1
#     return count

from math import log

def divisions(n, divisor):
    return int(log(n, divisor))


q = divisions(6, 2)  # 2
q
q = divisions(100, 2)  # 6
q
q = divisions(2450, 5)  # 4
q
q = divisions(9999, 3)  # 8
q
q = divisions(2, 3)  # 0
q
q = divisions(5, 5)  # 1
q
