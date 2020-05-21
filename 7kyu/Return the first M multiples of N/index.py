# 7kyu - Return the first M multiples of N

""" Implement a function, multiples(m, n), which returns an array of the first m multiples of the real number n. 
Assume that m is a positive integer.


multiples(3, 5.0)

should return

[5.0, 10.0, 15.0] """


# def multiples(m, n):
#     res = []
#     for i in range(1, m + 1):
#         res.append(i * n)
#     return res

def multiples(m, n):
    return [i * n for i in range(1, m + 1)]


q = multiples(3, 5)  # [5, 10, 15]
q
q = multiples(3, 5.0)  # [5.0, 10.0, 15.0]
q
