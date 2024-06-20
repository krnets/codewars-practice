def get_reversed_color(hex_color):
    assert len(hex_color) < 7
    color = int(hex_color or "0", 16)
    return f"#{color ^ 0xFFFFFF:06X}"
