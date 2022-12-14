def is_sorted_and_how(arr):
    is_ascending = arr[0] < arr[1]
    for i in range(1, len(arr)):
        if (arr[i - 1] > arr[i] and is_ascending) or \
           (arr[i - 1] < arr[i] and not is_ascending):
            return "no"
    return f'yes, {"ascending" if is_ascending else "descending"}'
