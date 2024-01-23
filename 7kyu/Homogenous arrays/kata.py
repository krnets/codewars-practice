# def filter_homogenous(arrays):
#     return [*filter(lambda x: x and all(isinstance(y, type(x[0])) for y in x), arrays)]


def is_homogenous(array):
    return len(set(map(type, array))) == 1


def filter_homogenous(arrays):
    return [*filter(is_homogenous, arrays)]
