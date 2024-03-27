from collections import Counter
from PIL import ImageColor


def get_colors(col_arr):
    res = []

    for arr in col_arr:
        d = Counter()
        for color in arr:
            r, g, b = ImageColor.getrgb("#" + color)
            m = max(r, g, b)
            if m == r: d["Red"] += 1
            elif m == g: d["Green"] += 1
            elif m == b: d["Blue"] += 1
        res.append("{}+{}".format(max(d, key=d.get), min(d, key=d.get)))

    return ",".join(res)
