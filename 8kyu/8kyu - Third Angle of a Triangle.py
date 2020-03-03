# 8kyu - Third Angle of a Triangle

""" You are given two angles (in degrees) of a triangle.

Write a function to return the 3rd.

Note: only positive integers will be tested. """


def other_angle(a, b):
    return 180 - (a + b)


q = other_angle(30, 60)  # 90
q
q = other_angle(60, 60)  # 60
q
q = other_angle(43, 78)  # 59
q
q = other_angle(10, 20)  # 150
q
