def bubblesort_once(l):
    arr = l.copy()
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
    return arr
