# def score_throws(radii):
#     points = 0
#     count_bonus = 0

#     for throw in radii:
#         if throw < 5:
#             points += 10
#             count_bonus += 1
#         elif throw <= 10:
#             points += 5

#     return points + 100 if radii and count_bonus == len(radii) else points


def score_throws(radii):
    points, count_bonus = 0, 0

    for throw in radii:
        points += (0, 5, 10)[(throw < 5) + (throw <= 10)]
        count_bonus += (0, 1)[throw < 5]

    return points + (0, 100)[bool(radii and count_bonus == len(radii))]
