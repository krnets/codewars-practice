# Beta - Simple: Find The Distance Between Two Points

""" Given two ordered pairs calculate the distance between them. 
Round to two decimal places. This should be easy to do in 0(1) timing. """

# from functools import reduce
# from math import hypot

# def distance(x1, y1, x2, y2):
#     return round(reduce(hypot, (x-y for x, y in ((x1, x2), (y1, y2)))), 2)

from math import hypot

def distance(x1, y1, x2, y2):
    return round(hypot(x2 - x1, y2 - y1), 2)


q = distance(1, 1, 0, 0)  # 1.41
q
