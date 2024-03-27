# def sum_arrays(array1, array2):
#     if len(array1) < len(array2):
#         array1, array2 = array2, array1

#     m, n = len(array1), len(array2)
#     res = [0] * max(m, n)
#     carry = 0

#     for i in range(1, len(res) + 1):
#         if i <= m:
#             if i <= n:
#                 s = array1[-i] + array2[-i]
#                 res[-i] = (carry + s) % 10
#                 carry = s // 10
#             else:
#                 res[-i] = (carry + array1[-i]) % 10
#                 carry = res[-i] // 10

#     return [1] + res if carry else res


# def sum_arrays(array1, array2):
#     if not array1: return array2
#     if not array2: return array1
#     a = int("".join(map(str, array1)))
#     b = int("".join(map(str, array2)))
#     n = a + b
#     res = [*map(int, str(abs(n)))]
#     res[0] *= (-1, 1)[n > 0]
#     return res


def sum_arrays(array1, array2):
    if not array1: return array2
    if not array2: return array1
    n = sum(map(lambda arr: int("".join(map(str, arr))), [array1, array2]))
    res = [*map(int, str(abs(n)))]
    res[0] *= (-1, 1)[n > 0]
    return res
