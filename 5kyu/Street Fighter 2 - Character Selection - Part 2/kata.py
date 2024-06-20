def super_street_fighter_selection(fighters, position, moves):
    empty_space = {
        (i, j)
        for i, row in enumerate(fighters)
        for j, fighter in enumerate(row)
        if not fighter
    }
    i, j = position
    m, n = len(fighters), len(fighters[0])
    res = []

    for move in moves:
        match move:
            case "up":
                i -= 1 if (i - 1, j) not in empty_space and i > 0 else 0
            case "down":
                i += 1 if (i + 1, j) not in empty_space and (i + 1) < m else 0
            case "left":
                j = (
                    (j - 1) % n
                    if (i, (j - 1) % n) not in empty_space
                    else (
                        (j - 2) % n
                        if (i, (j - 2) % n) not in empty_space
                        else (j - 3) % n
                    )
                )
            case "right":
                j = (
                    (j + 1) % n
                    if (i, (j + 1) % n) not in empty_space
                    else (
                        (j + 2) % n
                        if (i, (j + 2) % n) not in empty_space
                        else (j + 3) % n
                    )
                )
        res.append(fighters[i][j])

    return res
