def reverse_fun(n):
    arr = list(n)
    for i in range(len(arr)):
        arr = arr[:i] + list(reversed(arr[i:]))
    return "".join(arr)
