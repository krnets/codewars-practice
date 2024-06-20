# def types(x):
#     types = [bool, int, float, str]

#     for t in types:
#         if isinstance(x, t):
#             return t.__name__


# def types(x):
#     types = [bool, int, float, str]
#     return next(t.__name__ for t in types if isinstance(x, t))


def types(x):
    return type(x).__name__
