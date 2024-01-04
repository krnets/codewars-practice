# def combine(*dicts):
#     res = {}
#     for d in dicts:
#         for k, v in d.items():
#             if k in res:
#                 res[k] += v
#             else:
#                 res[k] = v
#     return res


# def combine(*dicts):
#     res = {}
#     for d in dicts:
#         for k, v in d.items():
#             res[k] = v + res.get(k, 0)
#     return res

# from collections import defaultdict
from collections import Counter
from functools import reduce
from operator import add


# def combine(*dicts):
#     res = defaultdict(int)
#     for d in dicts:
#         for k, v in d.items():
#             res[k] += v
#     return res


def combine(*dicts):
    return reduce(add, map(Counter, dicts))
