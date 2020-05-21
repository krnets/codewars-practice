# 6kyu - Element equals its index

""" Given a sorted array of distinct integers, write a function index_equals_value that returns 
the lowest index for which array[index] == index. 

Return -1 if there is no such index.

Your algorithm should be very performant.

[input] array of integers ( with 0-based nonnegative indexing )
[output] integer

input: [-8,0,2,5]
output: 2 # since array[2] == 2

input: [-1,0,3,6]
output: -1 # since no index in array satisfies array[index] == index

Random Tests Constraints:

Array length: 200 000
Amount of tests: 1 000
Time limit: 1.5 s """

# def index_equals_value(arr):
#     min = 0
#     max = len(arr)-1
#     while min < max:
#         i = (min + max) // 2
#         if i <= arr[i]:
#             max = i
#         else:
#             min = i + 1
#     return max if arr[max] == max else -1


# def binary_search(arr):
#     low = 0
#     high = len(arr)-1
#     while low < high:
#         mid = (low + high) // 2
#         if mid <= arr[mid]:
#             high = mid
#         else:
#             low = mid + 1
#     return high if arr[high] == high else -1

# def index_equals_value(arr):
#     return binary_search(arr)

# def index_equals_value(arr):
#     low, high = 0, len(arr)
#     while low < high:
#         mid = (low + high) // 2
#         if mid <= arr[mid]:
#             high = mid
#         else:
#             low = mid + 1
#     return low if low < len(arr) and arr[low] == low else -1

def index_equals_value(arr):
    low, high = 0, len(arr)-1
    while low < high:
        mid = (low + high) // 2
        if mid <= arr[mid]:
            high = mid
        else:
            low = mid + 1
    return low if arr[low] == low else -1


q = index_equals_value([-3, 0, 1, 3, 10]), 3
q
q = index_equals_value([-5, 1, 2, 3, 4, 5, 7, 10, 15]), 1
q
q = index_equals_value([9, 10, 11, 12, 13, 14]),  -1
q
q = index_equals_value([0, ]),  0
q
