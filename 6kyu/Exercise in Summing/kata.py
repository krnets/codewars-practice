def minimum_sum(values, n):
    return sum(sorted(values)[:n])


def maximum_sum(values, n):
    return sum(sorted(values)[-n:]) if n else 0