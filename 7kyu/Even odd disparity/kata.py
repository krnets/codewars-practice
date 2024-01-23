from itertools import filterfalse, tee


# def solve(a):
#     t1, t2 = tee(x for x in a if isinstance(x, int))
#     is_odd = lambda x: x & 1
#     return len([*filterfalse(is_odd, t1)]) - len([*filter(is_odd, t2)])


# def solve(a):
#     return sum(-1 if x & 1 else 1 for x in a if isinstance(x, int))


def solve(a):
    return sum((1, -1)[x & 1] for x in a if isinstance(x, int))
