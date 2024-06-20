# def up_array(arr):
#     if not arr or not all(0 <= x <= 9 for x in arr):
#         return None
#     return [*map(int, str(int("".join(map(str, arr))) + 1).rjust(len(arr), "0"))]


def up_array(arr):
    if not arr or not all(0 <= x <= 9 for x in arr):
        return None
    for i in reversed(range(len(arr))):
        if arr[i] < 9:
            arr[i] += 1
            return arr
        arr[i] = 0
    return [1] + arr
