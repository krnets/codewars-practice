from itertools import cycle
from string import ascii_lowercase as abc


# def encode(message, key):
#     indices = [abc.index(c) + 1 for c in message]
#     key_digits = map(int, str(key))
#     return [x + y for x, y in zip(indices, cycle(key_digits))]


def encode(message, key):
    offset = ord("a") - 1
    key_digits = map(int, str(key))
    return [ord(c) - offset + d for c, d in zip(message, cycle(key_digits))]
