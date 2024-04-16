def sort_time(arr):
    arr.sort(key=lambda p: p[0])
    res = []
    prev = "00:00"

    while arr:
        i = next((i for i, period in enumerate(arr) if period[0] >= prev), 0)
        res.append(arr.pop(i))
        prev = res[-1][-1]

    return res
