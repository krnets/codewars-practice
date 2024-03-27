# def grid_map(inp, op):
#     res = []

#     for row in inp:
#         new_row = []
#         for x in row:
#             new_row.append(op(x))
#         res.append(new_row)

#     return res


def grid_map(inp, op):
    return [[*map(op, row)] for row in inp]
