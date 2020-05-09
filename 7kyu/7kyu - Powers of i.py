# 7kyu - Powers of i

""" i is the imaginary unit, it is defined by i² = -1, 
therefore it is a solution to x²+1=0.

Write a function pofi that returns i to the power of a given non-negative integer 
in its simplest form as a string (answer may contain i). """


# def pofi(n):
#     if n % 4 == 0:
#         return '1'
#     elif n % 4 == 1:
#         return 'i'
#     elif n % 4 == 2:
#         return '-1'
#     elif n % 4 == 3:
#         return '-i'

# def pofi(n):
#     return '1 i -1 -i'.split()[n % 4]

# def pofi(n):
#     return ['1', 'i', '-1', '-i'][n % 4]

def pofi(n):
    return ('1', 'i', '-1', '-i')[n & 3]


q = pofi(0), '1'
q
q = pofi(1), 'i'
q
q = pofi(2), '-1'
q
q = pofi(3), '-i'
q
q = pofi(4), '1'
q
q = pofi(5), 'i'
q
q = pofi(6), '-1'
q
q = pofi(7), '-i'
q
q = pofi(8), '1'
q
q = pofi(9), 'i'
q
q = pofi(10), '-1'
q
