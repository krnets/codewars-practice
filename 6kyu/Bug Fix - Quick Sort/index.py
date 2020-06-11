""" 6kyu - Bug Fix - Quick Sort

There is an implementation of quicksort algorithm. Your task is to fix it. All inputs are correct. """


# def quicksort(arr):
#     if len(arr) < 2:
#         return arr
#     pivot = arr[0]
#     less = [i for i in arr[1:] if i <= pivot]
#     greater = [i for i in arr[1:] if i > pivot]
#     return quicksort(less) + [pivot] + quicksort(greater)

# def quicksort(arr):
#     if len(arr) < 1:
#         return arr
#     p = arr[0]
#     return quicksort(list(filter(lambda x: x <= p, arr[1:]))) + [p] + quicksort(list(filter(lambda x: x > p, arr[1:])))


# quicksort is an in-place sorting algorithm, so let's not create extra lists

# def quicksort(arr):
#     def inner(arr, start, end):
#         if start < end:
#             pivot = partition(arr, start, end)
#             inner(arr, start, pivot - 1)
#             inner(arr, pivot + 1, end)
#     inner(arr, 0, len(arr) - 1)
#     return arr

# def partition(arr, start, end):
#     pivot = arr[start]
#     left, right = start + 1, end
#     while True:
#         if left <= right and arr[left] <= pivot:
#             left += 1
#         if left <= right and pivot <= arr[right]:
#             right -= 1
#         if left > right:
#             arr[start], arr[right] = arr[right], arr[start]
#             return right
#         arr[left], arr[right] = arr[right], arr[left]

def quicksort(arr):
    def inner(arr, start, end):
        if start < end:
            pivot = partition(arr, start, end)
            inner(arr, start, pivot-1)
            inner(arr, pivot+1, end)
    inner(arr, 0, len(arr)-1)
    return arr


def partition(arr, start, end):
    pivot = arr[end]
    i, j = start-1, start
    while j <= end-1:
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    i += 1
    arr[i], arr[end] = arr[end], arr[i]
    return i


q = quicksort([1]), [1]
q
q = quicksort([]), []
q
q = quicksort([1, 5, 2]), [1, 2, 5]
q
q = quicksort([17, -5, 3]), [-5, 3, 17]
q
q = quicksort([3, 0, 7, 5, 1, 2, 9, 8, 4, 6]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
q
q = quicksort([17, -5, 3, 3]), [-5, 3, 3, 17]
q
