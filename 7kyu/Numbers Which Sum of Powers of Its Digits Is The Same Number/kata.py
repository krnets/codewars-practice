# def eq_sum_powdig(h_max, exp):
#     res = []
#     for x in range(10 ** (exp - 1), h_max + 1):
#         if x == sum(int(y) ** exp for y in str(x)):
#             res.append(x)
#     return res


def eq_sum_powdig(h_max, exp):
    return [x for x in range(100, h_max + 1) if x == sum(int(y) ** exp for y in str(x))]
