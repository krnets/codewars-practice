# 8kyu - Count by X

""" Create a function with two arguments that will return an array of the first (n) multiples of (x).
Assume both the given number and the number of times to count will be positive numbers greater than 0.
Return the results as a list in Python. """


# def count_by(x, n):
#     return [i * x for i in range(1, n + 1)]

def count_by(x, n):
    return list(range(x, n * x + 1, x))


q = count_by(1, 10)  # [1,2,3,4,5,6,7,8,9,10]
q
q = count_by(2, 5)  # [2,4,6,8,10]
q
q = count_by(1, 5)  # [1, 2, 3, 4, 5]
q
q = count_by(2, 5)  # [2, 4, 6, 8, 10]
q
q = count_by(3, 5)  # [3, 6, 9, 12, 15]
q
q = count_by(50, 5)  # [50, 100, 150, 200, 250]
q
q = count_by(100, 5)  # [100, 200, 300, 400, 500]
q
