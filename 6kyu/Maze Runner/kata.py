def maze_runner(maze, directions):
    n = len(maze)
    i, j = next((i, j) for i in range(n) for j in range(n) if maze[i][j] == 2)
    for direction in directions:
        match direction:
            case "N": i -= 1
            case "E": j += 1
            case "S": i += 1
            case "W": j -= 1
        if not 0 <= i < n or not 0 <= j < n or maze[i][j] == 1:
            return "Dead"
        if maze[i][j] == 3:
            return "Finish"
    return "Lost"