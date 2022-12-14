# def mygcd(x, y):
#     return x if not y else mygcd(y, x % y)

# from math import gcd as mygcd

def mygcd(x, y):
    while y:
        x, y = y, x % y
    return x

q = mygcd(30, 12)  # 6
q
q = mygcd(8, 9)  # 1
q
q = mygcd(1, 1)  # 1
q
