from collections import Counter


def paint_letterboxes(start, finish):
    digits = "".join(map(str, range(start, finish + 1)))
    res = [0] * 10

    for digit, count in Counter(digits).items():
        res[int(digit)] = count

    return res
