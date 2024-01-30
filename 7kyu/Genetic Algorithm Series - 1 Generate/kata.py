import random

def generate(length):
    return '{:0{}b}'.format(random.getrandbits(length), length) if length else ''