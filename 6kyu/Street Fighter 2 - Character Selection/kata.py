def street_fighter_selection(fighters, initial_position, moves):
    i, j = initial_position
    n = len(fighters[0])
    res = []
    for move in moves:
        match move:
            case "up":    i = 0
            case "down":  i = 1
            case "right": j = (j + 1) % n
            case "left":  j = (j - 1) % n
        res.append(fighters[i][j])
    return res