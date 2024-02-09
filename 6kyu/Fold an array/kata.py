# def fold_array(array, runs):
#     if not runs:
#         return array
#     n = len(array)
#     res = [array[i] + array[n - i - 1] for i in range(n // 2)]
#     if n & 1:
#         res.append(array[n // 2])
#     return fold_array(res, runs - 1)

# def fold_array(array, runs):
#     mid = len(array) // 2
#     a = [sum(pair) for pair in zip(array[:mid] + [0], reversed(array[mid:]))]
#     return fold_array(a, runs - 1) if runs > 1 else a


# def fold_array(array, runs):
#     mid = len(array) // 2
#     folded = [left + right for left, right in zip(array[:mid] + [0], reversed(array[mid:]))]
#     return folded if runs <= 1 else fold_array(folded, runs - 1)


def fold_array(array, runs):
    ret = array.copy()
    for _ in range(runs):
        mid = len(ret) // 2
        ret = [sum(pair) for pair in zip(ret[:mid] + [0], reversed(ret[mid:]))]
    return ret
