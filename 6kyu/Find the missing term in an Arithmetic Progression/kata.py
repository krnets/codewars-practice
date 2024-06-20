from itertools import pairwise


# def find_missing(sequence):
#     step = min(y - x for x, y in pairwise(sequence[:5]))

#     for x, y in pairwise(sequence):
#         if y - x != step:
#             return x + step
#     return 0


def find_missing(sequence):
    return (sequence[0] + sequence[-1]) * (len(sequence) + 1) // 2 - sum(sequence)
