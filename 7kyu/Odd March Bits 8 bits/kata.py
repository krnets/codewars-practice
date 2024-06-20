# def bit_march(n: int) -> list:
#     arr = []

#     for i in range(9 - n):
#         row = [0] * 8

#         for j in range(-i - 1, -i - n - 1, -1):
#             row[j] = 1

#         arr.append(row)

#     return arr

from collections import deque


def bit_march(n: int) -> list:
    dq = deque([1] + [0] * (8 - n) + [1] * (n - 1))

    return [dq.rotate(-1) or list(dq) for _ in range(8 - n + 1)]
