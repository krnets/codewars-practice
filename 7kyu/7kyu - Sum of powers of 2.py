# 7kyu - Sum of powers of 2

""" Given a number n, you should find a set of numbers for which the sum equals n. 
This set must consist exclusively of values that are a power of 2 (eg: 2^0 => 1, 2^1 => 2, 2^2 => 4, ...).

The function powers takes a single parameter, the number n, and should return an array of unique numbers.

Criteria

The function will always receive a valid input: any positive integer between 1 and the max integer value 
for your language (eg: for JavaScript this would be 9007199254740991 otherwise known as Number.MAX_SAFE_INTEGER).

The function should return an array of numbers that are a power of 2 (2^x = y).

Each member of the returned array should be unique. (eg: the valid answer for powers(2) is [2], not [1, 1])

Members should be sorted in ascending order (small -> large). (eg: the valid answer for powers(6) is [2, 4], not [4, 2]) 

return an array of numbers (that are a power of 2)
for which the input "n" is the sum """

# def powers(n):
#     res = []
#     v = 1
#     while n > 0:
#         if n % 2 == 1:
#             res.append(v)
#         n = n // 2
#         v *= 2
#     return res

# def powers(n):
#     return [pow(2, i) for i, x in enumerate(reversed(bin(n))) if x == '1']

# def powers(n):
#     return [2 ** i for i, x in enumerate(reversed(bin(n))) if x == '1']

# def powers(n):
#     return [1 << i for i, x in enumerate(reversed(bin(n))) if x == '1']

# def powers(n):
#     return [1 << i for i in range(n.bit_length()) if 1 << i & n]

# def powers(n):
#     return [1 << i for i, x in enumerate(f'{n:b}'[::-1]) if x == '1']

def powers(n):
    return [x << i for i, x in enumerate(map(int, reversed(f'{n:b}'))) if x]


q = powers(1), [1]
q
q = powers(2), [2]
q
q = powers(6), [2, 4]
q
q = powers(42)
q
