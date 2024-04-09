from itertools import cycle

def pair_zeros(arr):
    toggle = cycle([True, False])
    return [x for x in arr if x or next(toggle)]
