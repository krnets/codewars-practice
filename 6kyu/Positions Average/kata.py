from itertools import combinations


def pos_average(s):
    pairs = [*combinations(s.split(", "), 2)]
    count_in_common = sum(x == y for a, b in pairs for x, y in zip(a, b))
    m, n = len(pairs), len(pairs[0][0])
    return 100 * count_in_common / (m * n)
