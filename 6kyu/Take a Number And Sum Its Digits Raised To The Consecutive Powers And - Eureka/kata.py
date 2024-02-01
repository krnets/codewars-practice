# def sum_dig_pow(a, b):
#     res = []
#     for i in range(a, b + 1):
#         if sum(int(x) ** i for i, x in enumerate(str(i), 1)) == i:
#             res.append(i)
#     return res


def sum_dig_pow(a, b):
    return [*filter(eureka, range(a, b + 1))]


def eureka(n):
    return n == sum(int(x) ** i for i, x in enumerate(str(n), 1))
