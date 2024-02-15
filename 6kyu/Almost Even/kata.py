# def split_integer(num, parts):
#     smallest = num // parts
#     res = [smallest] * parts
#     hydrate = num - parts * smallest

#     for i in range(hydrate):
#         res[-i - 1] += 1
#     return res


def split_integer(num, parts):
    q, r = divmod(num, parts)
    return [q] * (parts - r) + [q + 1] * r
