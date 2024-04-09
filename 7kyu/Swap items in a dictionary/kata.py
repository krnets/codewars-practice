from collections import defaultdict


def switch_dict(dic):
    res = defaultdict(list)

    for k, v in dic.items():
        res[v].append(k)

    return res
