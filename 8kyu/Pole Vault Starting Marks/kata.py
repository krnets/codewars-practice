def starting_mark(height):
    x1, x2 = 1.52, 1.83
    y1, y2 = 9.45, 10.67
    offset = (x2 * y1 - x1 * y2) / (x2 - x1)
    slope = (y2 - y1) / (x2 - x1)
    return round(offset + height * slope, 2)
