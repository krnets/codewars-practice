# def consecutive(arr):
#     return abs(len(arr) - (max(arr) - min(arr)) - 1) if arr else 0


def consecutive(arr):
    return max(arr) - min(arr) + 1 - len(arr) if arr else 0
