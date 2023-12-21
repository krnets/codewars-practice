def is_madhav_array(arr):
    if len(arr) <= 2:
        return False

    first_num = arr[0]
    i = 1
    window_size = 2

    while i + window_size <= len(arr):
        current_sum = sum(arr[i : i + window_size])
        if current_sum != first_num:
            return False
        i += window_size
        window_size += 1

    return i == len(arr)
