# def growing_plant(upSpeed, downSpeed, desiredHeight):
#     plantHeight = 0
#     days = 0

#     while plantHeight < desiredHeight:
#         plantHeight += upSpeed
#         days += 1

#         if plantHeight >= desiredHeight:
#             return days

#         plantHeight -= downSpeed

#     return days

# def growing_plant(upSpeed, downSpeed, desiredHeight):
#     days = 1
#     plantHeight = upSpeed

#     while plantHeight < desiredHeight:
#         plantHeight += upSpeed -  downSpeed
#         days += 1

#     return days

from math import ceil

def growing_plant(upSpeed, downSpeed, desiredHeight):
    return max(1, ceil((desiredHeight - downSpeed) / (upSpeed - downSpeed)))


q = growing_plant(100, 10, 910)  # 10
q
q = growing_plant(10, 9, 4)  # 1
q
q = growing_plant(5, 2, 0)  # 1
q
q = growing_plant(5, 2, 5)  # 1
q
q = growing_plant(5, 2, 6)  # 2
q
