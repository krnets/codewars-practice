# def rgb(r, g, b):
#     r = max(0, min(255, r))
#     g = max(0, min(255, g))
#     b = max(0, min(255, b))
#     return ("{:02X}" * 3).format(r, g, b)


def rgb(r, g, b):
    clamp = lambda x: max(0, min(255, x))
    return ("{:02X}" * 3).format(*map(clamp, [r, g, b]))
