from itertools import chain


# def grid_index(grid, indexes):
#     flattened = [*chain.from_iterable(grid)]
#     return "".join(flattened[i - 1] for i in indexes)


# def grid_index(grid, indexes):
#     flattened = sum(grid, [])
#     return "".join(flattened[i - 1] for i in indexes)


def grid_index(grid, indexes):
    return "".join(
        grid[i][j] for i, j in map(lambda x: divmod(x - 1, len(grid)), indexes))