# import re

def is_valid_coordinates(coordinates):
    try:
        latitude, longitude = [float(c) for c in coordinates.split(",") if "e" not in c]
    except ValueError:
        return False
    return abs(latitude) <= 90 and abs(longitude) <= 180
