from math import ceil


# def new_avg(arr, newavg):
#     if not arr:
#         return newavg
#     avg = sum(arr) / len(arr)
#     if avg > newavg:
#         raise ValueError("Average of arr is already greater than newavg")
#     return ceil(newavg * (len(arr) + 1) - sum(arr))


def new_avg(arr, newavg):
    ans = ceil(newavg * (len(arr) + 1) - sum(arr))
    if ans < 0:
        raise ValueError("Average of arr is already greater than newavg")
    return ans
