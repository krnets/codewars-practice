import re

# def count_deaf_rats(town):
#     left, right = re.split("P", town)
#     going_left = [x for x in re.findall(r"[~O]{2}", left) if x == "O~"]
#     going_right = [x for x in re.findall(r"[~O]{2}", right) if x == "~O"]
#     return len(going_left) + len(going_right)


def count_deaf_rats(town):
    left, right = town.split("P")
    going_left = [x for x in re.findall(r"[~O]{2}", left) if x == "O~"]
    going_right = [x for x in re.findall(r"[~O]{2}", right) if x == "~O"]
    return len(going_left) + len(going_right)
