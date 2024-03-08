# def lstzip(a, b, fn):
#     return [*map(fn, *(a, b))]


# def lstzip(a, b, fn):
#     return [fn(*tup) for tup in zip(a, b)]


def lstzip(a, b, fn):
    return [*map(fn, a, b)]
