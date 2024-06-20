# def count_inversions(array):
#     return sum(
#         array[j] > array[i]
#         for i in range(len(array))
#         for j in range(i)
#     )


def count_inversions(array):
    return sum(y > x for i, x in enumerate(array) for y in array[:i])
