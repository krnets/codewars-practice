def hex_color(codes):
    if not codes:
        return "black"
    r, g, b = map(int, codes.split())
    if r + g + b == 0: return "black"
    if r == g and g == b: return "white"
    if r > g and r > b: return "red"
    if g > r and g > b: return "green"
    if b > r and b > g: return "blue"
    if r == g: return "yellow"
    if r == b: return "magenta"
    if g == b: return "cyan"
