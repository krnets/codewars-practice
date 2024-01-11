# def arithmetic_sequence_elements(a, d, n):
#     if d == 0:
#         return ", ".join(map(str, [a] * n))
#     arr = [str(i) for i in range(a, a + d * n, d)]
#     return ", ".join(arr)


# def arithmetic_sequence_elements(a, d, n):
#     return ", ".join(str(a + i * d) for i in range(n))

from itertools import count, islice


def arithmetic_sequence_elements(a, d, n):
    return ", ".join(map(str, islice(count(a, d), n)))
