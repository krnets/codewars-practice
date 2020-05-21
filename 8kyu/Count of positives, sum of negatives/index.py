# 8kyu - Count of positives / sum of negatives

""" Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.
Example

For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65]. """


# def count_positives_sum_negatives(arr):
#     res = [len(list(filter(lambda x: x > 0, arr))),
#            sum(list(filter(lambda x: x < 0, arr)))]
#     return [] if arr == [] else res

# def count_positives_sum_negatives(arr):
#     pos_count = neg_sum = 0
#     for x in arr:
#         if x > 0:
#             pos_count += 1
#         else:
#             neg_sum += x
#     return [] if not arr else [pos_count, neg_sum]

# def count_positives_sum_negatives(arr):
#     pos_count = neg_sum = 0
#     for x in arr:
#         if x > 0:
#             pos_count += 1
#         else:
#             neg_sum += x
#     return [pos_count, neg_sum] if len(arr) else []

# def count_positives_sum_negatives(arr):
#     pos_count = len(list(filter(lambda x: x > 0, arr)))
#     neg_sum   = sum(list(filter(lambda x: x < 0, arr)))
#     return [pos_count, neg_sum]

# def count_positives_sum_negatives(arr):
#     return [len(list(filter(lambda x: x > 0, arr))), sum(list(filter(lambda x: x < 0, arr)))]

# def count_positives_sum_negatives(arr):
#     return [len([x for x in arr if x > 0]), sum([x for x in arr if x < 0])] if arr else []

def count_positives_sum_negatives(arr):
    return [sum(x > 0 for x in arr), sum(y for y in arr if y < 0)] if arr else []


q = count_positives_sum_negatives(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])  # [10,-65]
q
q = count_positives_sum_negatives(
    [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14])  # [8,-50]
q
q = count_positives_sum_negatives([1])  # [1,0]
q
q = count_positives_sum_negatives([-1])  # [0,-1]
q
q = count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0])  # [0,0]
q
q = count_positives_sum_negatives([])  # []
q
