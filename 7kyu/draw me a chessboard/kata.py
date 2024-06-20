from itertools import cycle


def chess_board(rows, columns):
    squares = ["O", "X"]
    board = []

    for row_index in range(rows):
        it = cycle(reversed(squares)) if row_index & 1 else cycle(squares)
        row = [next(it) for _ in range(columns)]
        board.append(row)

    return board
