from itertools import pairwise


# def triangle(row):
#     if len(row) < 2:
#         return row

#     match_colours = {"BG": "R", "GB": "R", "RG": "B", "GR": "B", "BR": "G", "RB": "G"}
#     curr_row = list(row)

#     while len(curr_row) > 1:
#         next_row = []

#         for x, y in pairwise(curr_row):
#             next_row.append(match_colours.get(x + y, x))

#         curr_row = next_row

#     return curr_row.pop()


# def triangle(row):
#     if len(row) < 2:
#         return row

#     curr_row = list(row)

#     while len(curr_row) > 1:
#         next_row = []

#         for pair in pairwise(curr_row):
#             match pair:
#                 case "G", "B": next_row.append("R")
#                 case "B", "G": next_row.append("R")
#                 case "B", "R": next_row.append("G")
#                 case "R", "B": next_row.append("G")
#                 case "R", "G": next_row.append("B")
#                 case "G", "R": next_row.append("B")
#                 case _: next_row.append(pair[0])

#         curr_row = next_row

#     return curr_row.pop()

COLOURS = set("RGB")


def triangle(row):
    curr = list(row)

    while len(curr) > 1:
        curr = [x if x == y else (COLOURS - {x, y}).pop() for x, y in pairwise(curr)]

    return curr[0]
