# def denumerate(enum_list):
#     if not isinstance(enum_list, list):
#         return False
#     for x in enum_list:
#         if (
#             not isinstance(x, tuple)
#             or len(x) != 2
#             or not isinstance(x[0], int)
#             or not isinstance(x[1], str)
#             or len(x[1]) != 1
#             or not x[1].isalnum()
#         ):
#             return False
#     res = ""
#     for i, x in enumerate(sorted(enum_list)):
#         if x[0] != i:
#             return False
#         res += x[1]
#     return res


def denumerate(enum_list):
    try:
        idx_map = dict(enum_list)
        res = "".join(map(idx_map.get, range(mx := max(idx_map) + 1)))
        return (False, res)[res.isalnum() and len(res) == mx]
    except:
        return False

