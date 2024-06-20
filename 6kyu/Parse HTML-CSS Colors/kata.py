PRESET_COLORS = {
    "limegreen": "#32cd32",
    "blue": "#0000ff",
    "red": "#ff0000",
    "green": "#00ff00",
}


# def parse_html_color(color):
#     color_hex = PRESET_COLORS.get(color.lower(), color)

#     if len(color_hex) == 4:
#         r = int(color_hex[1] * 2, 16)
#         g = int(color_hex[2] * 2, 16)
#         b = int(color_hex[3] * 2, 16)
#     elif len(color_hex) == 7:
#         r = int(color_hex[1:3], 16)
#         g = int(color_hex[3:5], 16)
#         b = int(color_hex[5:7], 16)

#     return {"r": r, "g": g, "b": b}


def parse_html_color(color):
    color_hex = PRESET_COLORS.get(color.lower(), color)

    if len(color_hex) == 4:
        r, g, b = (int(color_hex[i] * 2, 16) for i in range(1, 4))
    elif len(color_hex) == 7:
        r, g, b = (int(color_hex[i : i + 2], 16) for i in range(1, 7, 2))

    return {"r": r, "g": g, "b": b}
