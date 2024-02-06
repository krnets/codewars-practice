from collections import Counter
from statistics import multimode

# def highest_rank(arr):
#     freq = Counter(arr)
#     max_count = max(freq.values())
#     return max(k for k, v in freq.items() if v == max_count)


# def highest_rank(arr):
#     return max(Counter(arr).items(), key=lambda item: (item[1], item[0]))[0]


def highest_rank(arr) -> int:
    return max(multimode(arr))
