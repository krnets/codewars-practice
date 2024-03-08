from itertools import permutations


def latest_clock(a, b, c, d):
    digits = "".join(map(str, [a, b, c, d]))
    valid_clocks = []

    for a, b, c, d in permutations(digits):
        if a + b < "24" and c + d < "60":
            valid_clocks.append(a + b + ":" + c + d)
            # valid_clocks.append("{}{}:{}{}".format(a, b, c, d))

    return max(valid_clocks, key=lambda x: (x[:2], x[2:]))