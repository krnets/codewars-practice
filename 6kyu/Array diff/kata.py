def array_diff(a, b):
    set_b = set(b)
    return [v for v in a if v not in set_b]
