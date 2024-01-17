from collections import Counter


def stanton_measure(arr):
    freq = Counter(arr)
    n = freq[1]
    return freq[n]
