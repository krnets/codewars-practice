""" 8kyu - Find Nearest square number

Find the nearest square number, nearest_sq(n), of a positive integer n. """


def nearest_sq(n):
    return round(n**0.5)**2


q = nearest_sq(1), 1
q
q = nearest_sq(2), 1
q
q = nearest_sq(10), 9
q
q = nearest_sq(111), 121
q
q = nearest_sq(9999), 10000
q
