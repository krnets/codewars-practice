# def parts_sums(ls):
#     return [sum(ls[i:]) for i in range(len(ls))] + [0]


# def parts_sums(ls):
#     total = sum(ls)
#     res = [total]
#     for v in ls:
#         total -= v
#         res.append(total)
#     return res


# def parts_sums(ls):
#     res = [sum(ls)]
#     for v in ls:
#         res.append(res[-1] - v)
#     return res

from itertools import accumulate

def parts_sums(ls):
    return [0, *accumulate(reversed(ls))][::-1]
