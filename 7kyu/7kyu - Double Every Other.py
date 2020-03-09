# 7kyu - Double Every Other

""" Write a function, that doubles every second integer in a list starting from the left. """


# def double_every_other(lst):
#     res = []
#     for i, x in enumerate(lst):
#         if i % 2 != 0:
#             res.append(x * 2)
#         else:
#             res.append(x)
#     return res

def double_every_other(lst):
    for i, v in enumerate(lst):
        if i % 2 != 0:
            lst[i] = v * 2
    return lst

# def double_every_other(lst):
#     return [x * 2 if i % 2 else x for i, x in enumerate(lst)]


q = double_every_other([1, 2, 3, 4, 5])  # [1,4,3,8,5]
q
q = double_every_other([1, 19, 6, 2, 12, -3])  # [1,38,6,4,12,-6]
q
q = double_every_other([-1000, 1653, 210, 0, 1])  # [-1000,3306,210,0,1]
q
