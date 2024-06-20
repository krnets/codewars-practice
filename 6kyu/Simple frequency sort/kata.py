from collections import Counter

def solve(arr):
    freq = Counter(arr)
    return sorted(arr, key=lambda x: (-freq[x], x))
