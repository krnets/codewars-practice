# from collections import OrderedDict

# def solve(arr):
#     return [*reversed(OrderedDict.fromkeys(reversed(arr)).keys())]


def solve(arr):
    return [*reversed(dict.fromkeys(reversed(arr)))]
