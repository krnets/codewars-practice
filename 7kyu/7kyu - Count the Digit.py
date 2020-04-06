# 7kyu - Count the Digit

""" Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer. 
Square all numbers k (0 <= k <= n) between 0 and n. 
Count the numbers of digits d used in the writing of all the k**2. 
Call nb_dig (or nbDig or ...) the function taking n and d as parameters and returning this count.

#Examples:

n = 10, d = 1, the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
We are using the digit 1 in 1, 16, 81, 100. The total count is then 4.

nb_dig(25, 1):
the numbers of interest are
1, 4, 9, 10, 11, 12, 13, 14, 19, 21 which squared are 1, 16, 81, 100, 121, 144, 169, 196, 361, 441
so there are 11 digits `1` for the squares of numbers between 0 and 25.

Note that 121 has twice the digit 1. """

# def nb_dig(n, d):
#     squared = map(lambda x: x * x, range(n+1))
#     return sum(1 for y in list(''.join(str(x) for x in squared)) if int(y) == d)

# def nb_dig(n, d):
#     squared = [x * x for x in range(n+1)]
#     return sum(1 for y in list(''.join(str(x) for x in squared)) if y == str(d))

# import re

# def nb_dig(n, d):
#     squared = [str(x * x) for x in range(n+1)]
#     str_num = ''.join(squared)
#     pattern = re.compile(str(d))
#     return len(re.findall(pattern, str_num))

# def nb_dig(n, d):
#     return sum(str(i * i).count(str(d)) for i in range(n+1))

# def nb_dig(n, d):
#     return ''.join(str(i ** 2) for i in range(n + 1)).count(str(d))


def nb_dig(n, d):
    return ''.join(str(i * i) for i in range(n + 1)).count(str(d))


q = nb_dig(5750, 0)  # 4700
q
q = nb_dig(11011, 2)  # 9481
q
q = nb_dig(12224, 8)  # 7733
q
q = nb_dig(11549, 1)  # 11905
q
