keyboard_layout = """
    a b c d e 1 2 3
    f g h i j 4 5 6
    k l m n o 7 8 9
    p q r s t . @ 0
    u v w x y z _ / """

key_pos = {
    c: (i, j)
    for i, row in enumerate(keyboard_layout.splitlines())
    for j, c in enumerate(row.split())
}


def tv_remote(word):
    return sum(
        abs(key_pos[x][0] - key_pos[y][0]) + abs(key_pos[x][1] - key_pos[y][1]) + 1
        for x, y in zip("a" + word, word)
    )
