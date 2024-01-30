# def sort_array(source_array):
#     odd_nums, odd_indices = [], []
#     for i, v in enumerate(source_array):
#         if v & 1:
#             odd_nums.append(v)
#             odd_indices.append(i)
#     for i, v in enumerate(sorted(odd_nums)):
#         idx = odd_indices[i]
#         source_array[idx] = v
#     return source_array


def sort_array(source_array):
    odd_nums = sorted(filter(lambda x: x & 1, source_array), reverse=True)
    return [odd_nums.pop() if x & 1 else x for x in source_array]

