# def duplicate_sandwich(arr):
#     start, end = [i for i, x in enumerate(arr) if arr.count(x) > 1]
#     return arr[start + 1 : end]


# def duplicate_sandwich(arr):
#     seen = dict()
#     for i, x in enumerate(arr):
#         if x in seen:
#             return arr[seen[x] : i]
#         else:
#             seen[x] = i + 1


def duplicate_sandwich(arr):
    seen = dict()
    for j, x in enumerate(arr):
        if i := seen.get(x):
            return arr[i:j]
        else:
            seen[x] = j + 1
