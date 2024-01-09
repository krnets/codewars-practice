from math import pi


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def circle_area(circle):
    return pi * circle.radius ** 2
