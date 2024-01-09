def move(self, direction):
    row, col = map(int, self.position)

    match direction:
        case 'up': row -= 1
        case 'down': row += 1
        case 'left': col -= 1
        case 'right': col += 1

    if not 0 <= row <= 4 or not 0 <= col <= 4:
        raise ValueError('Position out of bounds')

    self.position = f'{row}{col}'


Hero.move = move
