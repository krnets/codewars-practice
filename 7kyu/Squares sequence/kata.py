# def squares(x, n):
#     if n < 1:
#         return []
#     seq = [x]
#     for _ in range(n - 1):
#         x *= x
#         seq.append(x)
#     return seq


# def squares(x, n):
#     return [x ** (2**i) for i in range(n)]


# def squares(x, n):
#     seq = []
#     for _ in range(n):
#         seq.append(x)
#         x = x * x
#     return seq


def squares(x, n):
    return [] if n < 1 else [x] + squares(x * x, n - 1)
