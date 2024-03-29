# def gps(s, x):
#     max_speed = 0

#     for i in range(1, len(x)):
#         section_distance = x[i] - x[i-1]
#         section_speed = (3600 * section_distance) / s
#         max_speed = max(max_speed, section_speed)
    
#     return int(max_speed)

from itertools import pairwise

# def gps(s, x):
#     max_speed = 0

#     for x, y in pairwise(x):
#         section_distance = y - x
#         section_speed = (3600 * section_distance) / s
#         max_speed = max(max_speed, section_speed)
    
#     return int(max_speed)

def gps(s, x):
    return 0 if len(x) < 2 else max(y - x for x, y in pairwise(x)) * 3600 / s

x = [0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61]
s = 20
q = gps(s, x)  # 41
q
x = [0.0, 0.11, 0.22, 0.33, 0.44, 0.65, 1.08, 1.26, 1.68, 1.89, 2.1, 2.31, 2.52, 3.25]
s = 12
q = gps(s, x)  # 219
q
x = [0.0, 0.18, 0.36, 0.54, 0.72, 1.05, 1.26, 1.47, 1.92, 2.16, 2.4, 2.64, 2.88, 3.12, 3.36, 3.6, 3.84]
s = 20
q = gps(s, x)  # 80
q
x = [0.0, 0.01, 0.36, 0.6, 0.84, 1.05, 1.26, 1.47, 1.68, 1.89, 2.1, 2.31, 2.52, 2.73, 2.94, 3.15]
s = 14
q = gps(s, x)  # 90
q
x = [0.0, 0.02, 0.36, 0.54, 0.72, 0.9, 1.08, 1.26, 1.44, 1.62, 1.8]
s = 17
q = gps(s, x)  # 72
q
x = [0.0, 0.24, 0.48, 0.72, 0.96, 1.2, 1.44, 1.68, 1.92, 2.16, 2.4]
s = 12
q = gps(s, x)  # 72
q
x = [0.0, 0.02, 0.44, 0.66, 0.88, 1.1, 1.32, 1.54, 1.76]
s = 17
q = gps(s, x)  # 88
q
x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.32, 1.54, 1.76, 1.98, 2.2, 2.42, 2.76, 2.99, 3.22, 3.45]
s = 16
u = 76
q = gps(s, x)  # 76
q
x = [0.0, 0.01, 0.36, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75]
s = 17
q = gps(s, x)  # 82
q
x = [0.0, 0.2, 0.4, 0.69, 0.92, 1.15, 1.38, 1.61, 1.92, 2.16, 2.4, 2.64, 2.88, 3.12, 3.36]
s = 19
q = gps(s, x)  # 58
q
x = []
s = 19
q = gps(s, x)  # 0
q
x = [0.0]
s = 19
q = gps(s, x)  # 0
q
