def pattern(n):
    res, acc = [], ""
    for i in range(n, 0, -1):
        acc += str(i)
        res.append(acc)
    return "\n".join(res)
