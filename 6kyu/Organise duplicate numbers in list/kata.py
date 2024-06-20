from collections import Counter

def group(arr):
    return [[k] * v for k, v in Counter(arr).items()]
