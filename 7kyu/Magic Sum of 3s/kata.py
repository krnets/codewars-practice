def magic_sum(arr):
    return sum(x for x in arr if x & 1 and "3" in str(x))
