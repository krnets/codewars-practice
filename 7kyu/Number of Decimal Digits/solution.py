from math import log10

def digits(n):
    return int(n and log10(n)) + 1


q = digits(5)  # 1
q
q = digits(12345)  # 5
q
q = digits(9876543210)  # 10
q