# def trouble(x, t):
#     res = [x[0]]

#     for el in x[1:]:
#         if t - el != res[-1]:
#             res.append(el)

#     return res


def trouble(x, t):
    res = [x[0]]

    for elem in x[1:]:
        if res[-1] + elem != t:
            res.append(elem)

    return res
