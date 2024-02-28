# def histogram(values, bin_width):
#     if not values:
#         return values
#     res = [0] * (max(values) + 1)

#     for x in values:
#         res[x] += 1

#     return res if bin_width == 1 else [sum(res[i : i + bin_width]) for i in range(0, len(res), bin_width)]


def histogram(values, bin_width):
    res = [0] * (max(values, default=-1) // bin_width + 1)
    for x in values:
        res[x // bin_width] += 1
    return res
