# def tower_builder(n_floors):
#     w = n_floors + (n_floors - 1)
#     res = []
#     for i in range(n_floors):
#         floor = ("*" * i + "*" + "*" * i).rjust(w - n_floors + i + 1).ljust(w)
#         res.append(floor)
#     return res


# def tower_builder(n_floors):
#     w = n_floors + (n_floors - 1)
#     return [("*" * i + "*" + "*" * i).center(w) for i in range(n_floors)]


# def tower_builder(n_floors):
#     w = n_floors + (n_floors - 1)
#     return [("*" * (i * 2 - 1)).center(w) for i in range(1, n_floors + 1)]


def tower_builder(n_floors):
    w = n_floors + (n_floors - 1)
    return [("*" * i).center(w) for i in range(1, 2 * n_floors, 2)]
