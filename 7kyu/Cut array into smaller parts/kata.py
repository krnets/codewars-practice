# def make_parts(arr, chunk_size):
#     return [arr[i : i + chunk_size] for i in range(0, len(arr), chunk_size)]

# from itertools import batched

from itertools import islice


# def make_parts(arr, chunk_size):
#     return [*map(list, batched(arr, chunk_size))]


# def batched(iterable, n):
#     it = iter(iterable)
#     while batch := tuple(islice(it, n)):
#         yield batch


def make_parts(arr, chunk_size):
    return [*batched(arr, chunk_size)]


def batched(iterable, n):
    it = iter(iterable)
    while batch := list(islice(it, n)):
        yield batch
