from itertools import chain

# def bind(lst, func):
#     boxed = [*map(func, lst)]
#     return [*chain.from_iterable(boxed)]


# def bind(lst, func):
#     return [*chain(*map(func, lst))]


# def bind(lst, func):
#     res = []
#     for x in lst:
#         res.extend(func(x))
#     return res


# def bind(lst, func):
#     return [y for x in lst for y in func(x)]


def bind(lst, func):
    return sum(map(func, lst), [])
