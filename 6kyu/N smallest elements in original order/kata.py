from operator import itemgetter
import heapq

# def first_n_smallest(arr, n):
#     take_n = sorted((x, i) for i, x in enumerate(arr))[:n]
#     return [*map(itemgetter(0), sorted(take_n, key=itemgetter(1)))]


# def first_n_smallest(arr, n):
#     take_n = sorted((x, i) for i, x in enumerate(arr))[:n]
#     by_index, by_value = map(itemgetter, (0, 1))
#     return [*map(by_index, sorted(take_n, key=by_value))]


def first_n_smallest(arr, n):
    by_index, by_value = map(itemgetter, (0, 1))
    return [*map(by_value, sorted(heapq.nsmallest(n, enumerate(arr), key=by_value), key=by_index))]
