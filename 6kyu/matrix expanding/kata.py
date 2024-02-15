def expand(maze, fill):
    n = len(maze)
    padding_size = n // 2
    pad = [fill] * padding_size
    fresh_line = [fill] * (2 * n)

    for i in range(n):
        maze[i] = pad + maze[i] + pad

    for i in range(padding_size):
        maze.insert(0, fresh_line)
        maze.append(fresh_line)
    return maze
