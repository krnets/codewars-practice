from collections import Counter, defaultdict


# def delete_nth(order, max_e):
#     res, freq = [], Counter()
#     for x in order:
#         if x not in freq:
#             freq[x] = 1
#         else:
#             freq[x] += 1
#         if freq[x] <= max_e:
#             res.append(x)
#     return res


# def delete_nth(order, max_e):
#     res, freq = [], {}
#     for v in order:
#         n = freq.get(v, 0)
#         if n < max_e:
#             res.append(v)
#             freq[v] = n + 1
#     return res


def delete_nth(order, max_e):
    res, freq = [], defaultdict(int)
    for v in order:
        if freq[v] < max_e:
            res.append(v)
            freq[v] += 1
    return res
