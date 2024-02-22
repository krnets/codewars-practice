# def normalize(arr, fill_value=None):
#     n = max((len(sub) for sub in arr), default=0)

#     for i in range(len(arr)):
#         if len(arr[i]) < n:
#             arr[i].extend([fill_value] * (n - len(arr[i])))

#     return arr


def normalize(arr, fill_value=None):
    n = max(map(len, arr), default=0)
    return [sub + [fill_value] * (n - len(sub)) for sub in arr]
