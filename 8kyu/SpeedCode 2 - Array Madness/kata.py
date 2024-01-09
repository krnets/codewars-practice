def array_madness(a, b):
    return sum(x*x for x in a) > sum(x*x*x for x in b)