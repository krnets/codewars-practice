# def get_positions(n):
#     return tuple(n // i % 3 for i in (1, 3, 9))


def get_positions(n):
    return tuple(n // (3**i) % 3 for i in range(3))
