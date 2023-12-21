# def first_non_consecutive(arr):
#     for i, x in enumerate(arr[1:], 1):
#         if x - arr[i - 1] != 1:
#             return x
#     return None


def first_non_consecutive(arr):
    for i, x in enumerate(arr, arr[0]):
        if i != x:
            return x
