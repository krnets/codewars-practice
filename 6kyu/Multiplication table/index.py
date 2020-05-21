# 6kyu - Multiplication table

""" Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9

for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]] """


# def multiplicationTable(size):
#     table = []
#     for i in range(size):
#         row = []
#         for col in range(size):
#             row.append((col+1) * (i+1))
#         table.append(row)
#     return table

# def multiplicationTable(size):
#     return [[i * j for j in range(1, size+1)] for i in range(1, size+1)]

# def multiplicationTable(size):
#     return [[(x+1) * (y+1) for y in range(size)] for x in range(size)]

def multiplicationTable(size):
    return [[(row + 1) * (col + 1) for col in range(size)] for row in range(size)]


q = multiplicationTable(3)  # [[1,2,3],[2,4,6],[3,6,9]]
q
