def direction(facing, turn):
    angles = { 0: "N", 45: "NE", 90: "E", 135: "SE", 180: "S", 225: "SW", 270: "W", 315: "NW" }
    inverted_angles = {v: k for k, v in angles.items()}
    turned = inverted_angles.get(facing, 0) + turn
    return angles.get(turned % 360)
