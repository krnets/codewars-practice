# def swap_head_tail(arr):
#     mid = len(arr) // 2
#     if len(arr) == 1: return arr
#     if len(arr) & 1: return arr[-mid:] + [arr[mid]] + arr[:mid]
#     return arr[-mid:] + arr[:mid]


def swap_head_tail(arr):
    n, r = divmod(len(arr), 2)
    return arr[n + r :] + [arr[n]] * r + arr[:n]
