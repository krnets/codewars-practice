""" 7kyu - Halving Sum

Given a positive integer n, calculate the following sum:

n + n/2 + n/4 + n/8 + ...

All elements of the sum are the results of integer division.
Example

25  =>  25 + 12 + 6 + 3 + 1 = 47 """


# def halving_sum(n):
#     acc = 0
#     while n > 0:
#         acc += n
#         n //= 2
#     return acc

def halving_sum(n):
    return n and n + halving_sum(n >> 1)


q = halving_sum(25), 47
q
q = halving_sum(127), 247
q
