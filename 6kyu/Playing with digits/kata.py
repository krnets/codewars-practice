# def dig_pow(n, p):
#     k = sum(int(x) ** (p + i) for i, x in enumerate(str(n)))
#     return (-1, k // n)[k % n == 0]


def dig_pow(n, p):
    acc = sum(int(x) ** (p + i) for i, x in enumerate(str(n)))
    k, rem = divmod(acc, n)
    return k if rem == 0 else -1
