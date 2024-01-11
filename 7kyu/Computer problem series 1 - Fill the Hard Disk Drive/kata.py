# def save(sizes, hd_capacity):
#     hd_curr_size = 0
#     files_count = 0

#     for file_size in sizes:
#         hd_curr_size += file_size

#         if hd_curr_size > hd_capacity:
#             break
#         files_count += 1

#     return files_count

# from bisect import bisect
from itertools import accumulate, takewhile


# def save(sizes, hd_capacity):
#     return bisect(list(accumulate(sizes)), hd_capacity)


# def save(sizes, hd):
#     for i, size in enumerate(sizes):
#         if hd < size:
#             return i
#         hd -= size
#     return len(sizes)


def save(sizes, hd):
    return len([x for x in takewhile(lambda s: s <= hd, accumulate(sizes))])
