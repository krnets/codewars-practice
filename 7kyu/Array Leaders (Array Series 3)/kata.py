def array_leaders(numbers):
    res = []
    sum = 0

    for n in reversed(numbers):
        if n > sum:
            res.append(n)
        sum += n

    return [*reversed(res)]
