# 7kyu - Powers of 3

""" Given a positive integer N, return the largest integer k such that 3^k < N.

You may assume that the input to your function is always a positive integer. """


# def largest_power(N):
#     res = 0
#     while pow(3, res) < N:
#         res += 1
#     return res - 1


from math import ceil, log


def largest_power(N):
    return ceil(log(N, 3)) - 1


q = largest_power(3), 0
q
q = largest_power(4), 1
q
q = largest_power(5), 1
q
q = largest_power(8), 1
q
q = largest_power(12), 2
q
q = largest_power(42), 3
q
q = largest_power(1042), 6
q
