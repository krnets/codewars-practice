# def is_valid_walk(walk):
#     if len(walk) != 10:
#         return False
#     x, y = 0, 0
#     for step in walk:
#         match step:
#             case "n": y += 1
#             case "s": y -= 1
#             case "w": x += 1
#             case "e": x -= 1
#     return x == 0 and y == 0

from collections import Counter


def is_valid_walk(walk):
    counter = Counter(walk)
    return len(walk) == 10 and counter["n"] == counter["s"] and counter["w"] == counter["e"]