# def get_score(n):
#     res = 0
#     for i in range(1, n + 1):
#         res += i * 50
#     return res


def get_score(n):
    return n * (n + 1) * 25
