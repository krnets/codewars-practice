# def decode_resistor_colors(bands):
#     color_codes = { "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9, "gold": 5, "silver": 10 }
#     vals = [*map(color_codes.get, bands.split())]
#     ohms = int("{}{}".format(*vals[:2])) * 10 ** (vals[2] if len(vals) >= 2 else 0)
#     k, m = 1000, 1_000_000
#     k_or_m = ("", "k", "M")[(ohms >= k) + (ohms >= m)]
#     ohms = (ohms, ohms / k, ohms / m)[(ohms >= k) + (ohms >= m)]

#     return "{:g}{} ohms, {}%".format(ohms, k_or_m, vals[3] if len(vals) > 3 else 20)


def decode_resistor_colors(bands):
    color_codes = { "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5,
        "blue": 6, "violet": 7, "gray": 8, "white": 9, "gold": 5, "silver": 10 }
    vals = [*map(color_codes.get, bands.split())] + [20]
    ohms = int("{}{}".format(*vals[:2])) * 10 ** vals[2]
    suffix = ""
    for c in "kM":
        if ohms // 1000:
            ohms /= 1000
            suffix = c

    return f"{ohms:g}{suffix} ohms, {vals[3]}%"
