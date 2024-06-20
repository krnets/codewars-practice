# def array_conversion(arr):
#     p = 0

#     while len(arr) > 1:
#         if p & 1:
#             arr = [arr[i] * arr[i + 1] for i in range(0, len(arr), 2)]
#         else:
#             arr = [arr[i] + arr[i + 1] for i in range(0, len(arr), 2)]
#         p += 1

#     return arr.pop()


# def array_conversion(arr):
#     op = 0

#     while len(arr) > 1:
#         arr = [(x + y, x * y)[op] for x, y in zip(arr[::2], arr[1::2])]
#         op ^= 1

#     return arr.pop()

from itertools import cycle
from operator import add, mul


def array_conversion(arr):
    for op in cycle([add, mul]):
        arr = [op(*xy) for xy in zip(*[iter(arr)] * 2)]
        if len(arr) < 2:
            break

    return arr.pop()
