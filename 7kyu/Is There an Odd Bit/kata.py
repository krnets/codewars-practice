# def any_odd(x):
#     return bool(x & int("0b" + "10" * 8, 2))

def any_odd(x):
    return bool(x & 0xAAAA)
