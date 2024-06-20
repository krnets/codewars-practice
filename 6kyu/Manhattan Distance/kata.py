# def manhattan_distance(pointA, pointB):
#     ax, ay = pointA
#     bx, by = pointB
#     return abs(ax - bx) + abs(ay - by)

from scipy.spatial.distance import cityblock as manhattan_distance
