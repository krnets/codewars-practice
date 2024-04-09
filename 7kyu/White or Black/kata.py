# def square_color(file, rank):
#     c, r, board = "a", "1", {}

#     for i in range(8):
#         for j in range(8):
#             cell_file = f"{chr(ord(c)+j)}{chr(ord(r)+i)}"
#             cell_rank = f"{'white' if i & 1 ^ j & 1 else 'black'}"
#             board[cell_file] = cell_rank

#     return board[file + str(rank)]


# def square_color(file, rank):
#     return ("black", "white")[ord(file) & 1 ^ rank & 1]


def square_color(file, rank):
    return ("black", "white")[(ord(file) + rank) & 1]
