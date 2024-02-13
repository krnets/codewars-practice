def compute_depth(n):
    digits = set()
    steps = 0

    while len(digits) < 10:
        steps += 1
        t = n * steps
        while t:
            t, r = divmod(t, 10)
            digits.add(r)

    return steps
