def max_sum(arr, ranges):
    return max(sum(arr[i : j + 1]) for i, j in ranges)
