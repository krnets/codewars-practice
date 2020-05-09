# 7kyu - Area of a Circle

""" Complete the function circleArea so that it will return the area of a circle with the given radius. 
Round the returned number to two decimal places.
If the radius is not positive or not a number, return false. """

import math

def circleArea(r):
    return round((math.pi * r ** 2), 2) if isinstance(r, int) and r > 0 else False


q = circleArea(-1485.86)  # returns false
q
q = circleArea(0)  # returns false
q
q = circleArea(43.2673)  # returns 5881.25
q
q = circleArea(68)  # returns 14526.72
q
q = circleArea("number")  # returns false
q
