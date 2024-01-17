# def pendulum(values):
#     res = []
#     flag = False
#     for x in sorted(values):
#         if flag:
#             res.append(x)
#         else:
#             res.insert(0, x)
#         flag = not flag
#     return res

from collections import deque


# def pendulum(values):
#     dq = deque()
#     for i, x in enumerate(sorted(values)):
#         dq.append(x) if i & 1 else dq.appendleft(x)
#     return list(dq)


def pendulum(values):
    values.sort()
    return list(reversed(values[::2])) + values[1::2]
