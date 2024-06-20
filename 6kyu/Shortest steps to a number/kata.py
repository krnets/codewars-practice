def shortest_steps_to_num(num):
    if num < 2:
        return 0
    return 1 + shortest_steps_to_num((num // 2, num - 1)[num & 1])
