from itertools import pairwise


def range_extractor(lst):
    if len(lst) == 0:
        return "range(0)"
    if (
        not all(isinstance(x, int) for x in lst)
        or sum(lst) == 0
        or len(set(b - a for a, b in pairwise(lst))) != 1
    ):
        return False

    if len(lst) == 1:
        return "range(1)"
    a, b, z = lst[0], lst[1], lst[-1]
    step = b - a

    if step < 0:
        if abs(step) == 1:
            return f"range({a},{z + b})"
        return f"range({a},{z+step},{step})"

    if abs(step) == 1:
        if a == 0:
            return f"range({z+1})"
        return f"range({a},{z+1})"

    return f"range({a},{z+step},{step})"
