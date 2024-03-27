# def strange_math(n, k):
#     seq = sorted(map(str, range(1, n + 1)))
#     return seq.index(str(k)) + 1


# def strange_math(n, k):
#     return sorted(range(n + 1), key=str).index(k)


def strange_math(n, k):
    return sorted(map(str, range(n + 1))).index(str(k))
