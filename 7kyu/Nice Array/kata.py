def is_nice(arr):
    return len(arr) > 1 and all(x - 1 in arr or x + 1 in arr for x in arr)
