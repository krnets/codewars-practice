# def rgb_sum(color):
#     return sum(int(color[i : i + 2], 16) for i in range(1, len(color)))


# def brightest(colors):
#     return max(colors, key=lambda c: max(c[1:3], c[3:5], c[5:]))

from matplotlib.colors import to_rgb


def brightest(colors):
    return max(colors, key=lambda c: max(to_rgb(c)))
