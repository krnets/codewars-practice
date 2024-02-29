def find_even_index(arr):
    sum_right = sum(arr)
    sum_left = 0

    for i, x in enumerate(arr):
        sum_right -= x
        if sum_left == sum_right:
            return i
        sum_left += x

    return -1
