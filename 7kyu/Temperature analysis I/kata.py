# def lowest_temp(t):
#     return min(map(int, t.split())) if t else None


def lowest_temp(t):
    return min(map(int, t.split()), default=None)
