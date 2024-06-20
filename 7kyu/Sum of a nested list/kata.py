# def sum_nested(lst):
#     if not lst:
#         return 0
#     ans = 0

#     for x in lst:
#         if isinstance(x, list):
#             ans += sum_nested(x)
#         else:
#             ans += x

#     return ans


# def sum_nested(lst):
#     if not lst:
#         return 0
#     return sum(sum_nested(x) if isinstance(x, list) else x for x in lst)


def sum_nested(lst):
    return sum(sum_nested(x) if isinstance(x, list) else x for x in lst)
