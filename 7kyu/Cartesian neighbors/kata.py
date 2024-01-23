# def cartesian_neighbor(x, y):
#     return [
#         (x - 1, y - 1),
#         (x - 1, y),
#         (x - 1, y + 1),
#         (x, y - 1),
#         (x, y + 1),
#         (x + 1, y - 1),
#         (x + 1, y),
#         (x + 1, y + 1),
#     ]

from itertools import product


# def cartesian_neighbor(x, y):
#     return [z for z in product(range(x - 1, x + 2), range(y - 1, y + 2)) if z != (x, y)]

# def cartesian_neighbor(x, y):
#     return [*filter(lambda z: z != (x, y), product(range(x - 1, x + 2), range(y - 1, y + 2)))]


def cartesian_neighbor(x, y):
    res = [*product(range(x - 1, x + 2), range(y - 1, y + 2))]
    return res.pop(len(res) // 2) and res


#     return [*filter(lambda z: z != (x, y), product(range(x - 1, x + 2), range(y - 1, y + 2)))]
