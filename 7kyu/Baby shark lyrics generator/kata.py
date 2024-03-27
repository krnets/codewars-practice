def baby_shark_lyrics():
    x = ['Baby','Mommy','Daddy','Grandma','Grandpa']
    for i in range(5):
        x[i] += ' shark'
    x.append("Let's go hunt")
    o = ''
    for s in x:
        for _ in range(3):
            o += f"{s},{' doo' * 6}\n"
        o += f"{s}!\n"
    return o + "Run away,…"