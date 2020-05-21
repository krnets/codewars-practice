# 7kyu - Digitize

""" Given a non-negative integer, return a list of the individual digits in order. """


def digitize(n):
    return list(map(int, str(n)))

# def digitize(n):
#     return [int(d) for d in str(n)]


q = digitize(123)  # [1,2,3]
q
q = digitize(1)  # [1]
q
q = digitize(8675309)  # [8,6,7,5,3,0,9]
q
