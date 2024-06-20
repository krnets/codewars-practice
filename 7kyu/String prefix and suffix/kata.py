# def solve(st):
#     for i in range(len(st) // 2, 0, -1):
#         if st[:i] == st[-i:]:
#             return i
#     return 0


def solve(st):
    return next((i for i in range(len(st) // 2, 0, -1) if st[:i] == st[-i:]), 0)
