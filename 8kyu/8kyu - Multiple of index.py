# 8kyu - Multiple of index

""" Return a new array consisting of elements which are multiple of their own index in input array (length > 1).

Some cases:

[22, -6, 32, 82, 9, 25] =>  [-6, 32, 25]

[68, -1, 1, -7, 10, 10] => [-1, 10]

[-56,-85,72,-26,-14,76,-27,72,35,-21,-67,87,0,21,59,27,-92,68] => [-85, 72, 0, 68] """


# def multiple_of_index(arr):
#     res = []
#     for i in range(1, len(arr)):
#         if arr[i] % i == 0:
#             res.append(arr[i])
#     return res

# def multiple_of_index(arr):
#     return [n for i, n in enumerate(arr[1:], 1) if n % i == 0]

# def multiple_of_index(arr):
#     return [n for i, n in enumerate(arr) if i and not n % i]

def multiple_of_index(arr):
    return [n for i, n in enumerate(arr) if i and n % i == 0]


q = multiple_of_index([22, -6, 32, 82, 9, 25])  # [-6, 32, 25]
q
q = multiple_of_index([68, -1, 1, -7, 10, 10])  # [-1, 10]
q
q = multiple_of_index([11, -11])  # [-11]
q
q = multiple_of_index([-56, -85, 72, -26, -14, 76, -27, 72,
                       35, -21, -67, 87, 0, 21, 59, 27, -92, 68])  # [-85, 72, 0, 68]
q
q = multiple_of_index([28, 38, -44, -99, -13, -54, 77, -51])  # [38, -44, -99]
q
q = multiple_of_index([-1, -49, -1, 67, 8, -60, 39, 35])  # [-49, 8, -60, 35]
q
