# def find_screen_height(width, ratio):
#     w_ratio, h_ratio = map(int, ratio.split(":"))
#     height = int(width / w_ratio * h_ratio)
#     return f"{width}x{height}"


def find_screen_height(width, ratio):
    w_ratio, h_ratio = map(int, ratio.split(":"))
    height = h_ratio * width // w_ratio
    return f"{width}x{height}"
