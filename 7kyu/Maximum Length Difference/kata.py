def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1

    lengths1 = [*map(len, a1)]
    lengths2 = [*map(len, a2)]
    diff1 = max(lengths1) - min(lengths2)
    diff2 = max(lengths2) - min(lengths1)

    return max(diff1, diff2)
