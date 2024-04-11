# def cat_mouse(x, j):
#     dog_pos = x.find("D")
#     cat_pos = x.find("C")
#     mouse_pos = x.find("m")
#     if -1 in (dog_pos, cat_pos, mouse_pos):
#         return "boring without all three"
#     if abs(mouse_pos - cat_pos) > j:
#         return "Escaped!"
#     if cat_pos < dog_pos < mouse_pos or mouse_pos < dog_pos < cat_pos:
#         return "Protected!"
#     return "Caught!"


def cat_mouse(x, j):
    # dog, cat, mouse = (x.find(c) for c in "DCm")
    dog, cat, mouse = map(x.find, "DCm")
    if -1 in (dog, cat, mouse):
        return "boring without all three"
    if abs(mouse - cat) > j:
        return "Escaped!"
    return "Protected!" if cat < dog < mouse or mouse < dog < cat else "Caught!"
