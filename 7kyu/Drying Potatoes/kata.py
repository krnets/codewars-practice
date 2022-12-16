def potatoes(p0, w0, p1):
    return w0 * (100 - p0) // (100 - p1)


q = potatoes(82, 127, 80)  # 114
q
q = potatoes(93, 129, 91)  # 100
q
q = potatoes(99, 100, 98)  # 50
q