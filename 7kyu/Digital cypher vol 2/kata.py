from itertools import cycle
from string import ascii_lowercase


# def decode(code, key):
#     offset = ord("a") - 1
#     key_digits = map(int, str(key))
#     chars = [chr(x + offset - d) for x, d in zip(code, cycle(key_digits))]
#     return "".join(chars)


def decode(code, key):
    keys = cycle(map(int, str(key)))
    return "".join(ascii_lowercase[n - next(keys) - 1] for n in code)
