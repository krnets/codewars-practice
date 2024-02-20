# def move_zeros(lst):
#     i, j = 0, 1

#     while j < len(lst):
#         if lst[i] != 0:
#             i += 1
#         if lst[i] == 0 and lst[j] != 0:
#             lst[i], lst[j] = lst[j], lst[i]
#             i += 1
#         j += 1

#     return lst


# 1, 0, 1, 2
#    i  j
# 1, 1, 0, 2
#       i  j
# 1, 1, 2, 0


def move_zeros(lst):
    return sorted(lst, key=lambda x: not x)
