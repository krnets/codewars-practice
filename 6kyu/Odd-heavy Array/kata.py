from itertools import filterfalse

# def is_odd_heavy(arr):
#     is_odd = lambda x: x & 1
#     odds = [*filter(is_odd, arr)]
#     if not odds:
#         return False
#     smallest_odd = min(odds)
#     evens = [*filterfalse(is_odd, arr)]
#     return all(smallest_odd > x for x in evens)


def is_odd_heavy(arr):
    odds, evens = [], []
    for x in arr:
        if x & 1: odds.append(x)
        else: evens.append(x)
    return bool(odds) and min(odds) > max(evens, default=float("-inf"))
