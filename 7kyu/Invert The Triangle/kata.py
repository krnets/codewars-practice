from random import randrange

def invert_triangle(triangle):
    return triangle.translate(str.maketrans(" #", "# "))[::-1]


def maketri(s):
    space = s - 1
    if s % 2 == 0:
        mid = 2
    else:
        mid = 1
    tri = ""
    if randrange(0, 2) == 1:
        spac = " "
        haSh = "#"
    else:
        spac = "#"
        haSh = " "
    for k in range(s):
        tri += (spac * space) + haSh * mid + (spac * space) + "\n"
        mid += 2
        space -= 1
    return tri
