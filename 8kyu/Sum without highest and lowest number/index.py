# 8kyu - Sum without highest and lowest number

""" Sum all the numbers of the array except the highest and the lowest element (the value, not the index!).
(The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)

Example:

{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6

If array is empty, null or None, or if only 1 Element exists, return 0. """

# def sum_array(arr):
#     if not arr: return 0
#     return sum(sorted(arr)[1:-1])

# def sum_array(arr):
#     if arr == None or len(arr) < 3:
#         return 0
#     return sum(arr) - max(arr) - min(arr)

# def sum_array(arr):
#     return 0 if arr == None else sum(sorted(arr)[1:-1])

# def sum_array(arr):
#     return sum(sorted(arr)[1:-1]) if arr else 0

def sum_array(arr):
    return sum(sorted(arr or [])[1:-1])


q = sum_array(None)  # 0
q
q = sum_array([])  # 0
q
q = sum_array([3])  # 0
q
q = sum_array([-3])  # 0
q
q = sum_array([3, 5])  # 0
q
q = sum_array([-3, -5])  # 0
q
q = sum_array([6, 2, 1, 8, 10])  # 16
q
q = sum_array([6, 0, 1, 10, 10])  # 17
q
q = sum_array([-6, -20, -1, -10, -12])  # -28
q
q = sum_array([-6, 20, -1, 10, -12])  # 3
q
