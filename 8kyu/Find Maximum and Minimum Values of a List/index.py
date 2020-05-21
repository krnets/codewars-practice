# 8kyu - Find Maximum and Minimum Values of a List

""" Your task is to make two functions, max and min that take a(n) array/vector of integers list as input and outputs, 
respectively, the largest and lowest number in that array/vector.

maximun([4,6,2,1,9,63,-134,566]) returns 566
minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110
maximun([5]) returns 5
minimun([42, 54, 65, 87, 0]) returns 0

    You may consider that there will not be any empty arrays/vectors. """


# def minimun(arr):
#     low = float("inf")
#     for i in arr:
#         if i < low:
#             low = i
#     return low

# def maximun(arr):
#     high = float("-inf")
#     for i in arr:
#         if i > high:
#             high = i
#     return high

def minimun(arr):
    low = arr[0]
    for i in arr[1:]:
        if i < low:
            low = i
    return low

def maximun(arr):
    high = arr[0]
    for i in arr[1:]:
        if i > high:
            high = i
    return high

# def minimun(arr):
#     return list(sorted(arr))[0]

# def maximun(arr):
#     return list(sorted(arr))[-1]


q = minimun([-52, 56, 30, 29, -54, 0, -110])  # -110
q
q = minimun([42, 54, 65, 87, 0])  # 0
q
q = minimun([1, 2, 3, 4, 5, 10])  # 1
q
q = minimun([-1, -2, -3, -4, -5, -10])  # -10
q
q = minimun([9])  # 9
q

q = maximun([-52, 56, 30, 29, -54, 0, -110])  # 56
q
q = maximun([4, 6, 2, 1, 9, 63, -134, 566])  # 566
q
q = maximun([5])  # 5
q
q = maximun([534, 43, 2, 1, 3, 4, 5, 5, 443, 443, 555, 555])  # 555
q
q = maximun([9])  # 9
q
