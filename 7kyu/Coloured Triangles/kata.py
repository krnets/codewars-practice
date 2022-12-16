from itertools import pairwise

# def triangle(row):
#     while len(row) > 1:
#         next_row = []
#         for x, y in pairwise(row):
#             if x == y:
#                 next_row.append(x)
#             elif (x == "R" and y == "G") or (x == "G" and y == "R"):
#                 next_row.append("B")
#             elif (x == "G" and y == "B") or (x == "B" and y == "G"):
#                 next_row.append("R")
#             elif (x == "B" and y == "R") or (x == "R" and y == "B"):
#                 next_row.append("G")
#         row = next_row
#     return row[0]

# def triangle(row):
#     if len(row) == 1:
#         return row[0]

#     next_row = []

#     for x, y in pairwise(row):
#         if x == y:
#             next_row.append(x)
#         elif (x == "R" and y == "G") or (x == "G" and y == "R"):
#             next_row.append("B")
#         elif (x == "G" and y == "B") or (x == "B" and y == "G"):
#             next_row.append("R")
#         elif (x == "B" and y == "R") or (x == "R" and y == "B"):
#             next_row.append("G")

    # return triangle(next_row)

# def triangle(row):
#     if len(row) == 1:
#         return row[0]

#     next_row = []

#     for pair in pairwise(row):
#         match pair:
#             case 'R', 'G': next_row.append('B')
#             case 'G', 'R': next_row.append('B')
#             case 'G', 'B': next_row.append('R')
#             case 'B', 'G': next_row.append('R')
#             case 'R', 'B': next_row.append('G')
#             case 'B', 'R': next_row.append('G')
#             case _: next_row.append(pair[0])

#     return triangle(next_row)

def triangle(row):
    while len(row) > 1:
        next_row = []
        for pair in pairwise(row):
            match pair:
                case 'R', 'G': next_row.append('B')
                case 'G', 'R': next_row.append('B')
                case 'G', 'B': next_row.append('R')
                case 'B', 'G': next_row.append('R')
                case 'R', 'B': next_row.append('G')
                case 'B', 'R': next_row.append('G')
                case _: next_row.append(pair[0])
        row = next_row
    return row[0] if row else '_'


q = triangle("GB")  # 'R'
q
q = triangle("RRR")  # 'R'
q
q = triangle("RGBG")  # 'B'
q
q = triangle("RBRGBRB")  # 'G'
q
q = triangle("RBRGBRBGGRRRBGBBBGG")  # 'G'
q
q = triangle("B")  # 'B'
q
