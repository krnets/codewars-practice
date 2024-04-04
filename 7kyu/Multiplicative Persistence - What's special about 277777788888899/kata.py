from math import prod

def per(n):
    res = []
    while n > 9:
        n = prod(map(int, str(n)))
        res.append(n)
    return res
