from collections import Counter


def odd_ones_out(numbers):
    freq = Counter(numbers)
    return [v for v in numbers if not freq[v] & 1]
