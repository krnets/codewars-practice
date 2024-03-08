# def you_are_a_cube(cube):
#     base = int(cube ** (1 / 3))
#     return (base + (base**3 < cube)) ** 3 == cube


# def you_are_a_cube(cube):
#     return round(cube ** (1 / 3)) ** 3 == cube

from math import cbrt


def you_are_a_cube(cube):
    return round(cbrt(cube)) ** 3 == cube
