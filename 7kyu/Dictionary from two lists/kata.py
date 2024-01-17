from itertools import zip_longest


# def create_dict(keys, values):
#     return {k: v for k, v in zip_longest(keys, values) if k}


def create_dict(keys, values):
    return dict(zip_longest(keys, values[: len(keys)]))
