# def count_salutes(hallway):
#     end = hallway.rfind("<") + 1
#     idx = [i for i in range(end) if hallway[i] == ">"]
#     return sum(2 for i in idx for j in range(i + 1, end) if hallway[j] == "<")


def count_salutes(hallway):
    left, right = 0, 0
    for x in hallway:
        if   x == "<": left += 2 * right
        elif x == ">": right += 1
    return left
