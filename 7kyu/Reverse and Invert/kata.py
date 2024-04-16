def reverse_invert(lst):
    return [int(str(abs(x))[::-1]) * (-1, 1)[x < 0] for x in lst if isinstance(x, int)]
