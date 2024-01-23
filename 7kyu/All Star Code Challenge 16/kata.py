from collections import Counter


# def no_repeat(string):
#     for k, v in Counter(string).items():
#         if v == 1:
#             return k


def no_repeat(string):
    return next(k for k, v in Counter(string).items() if v == 1)
