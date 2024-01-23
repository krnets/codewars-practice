from math import prod
from operator import itemgetter


# def sort_by_value_and_index(arr):
#     arr_with_product = [(v, i * v) for i, v in enumerate(arr, 1)]
#     return [*map(itemgetter(0), sorted(arr_with_product, key=itemgetter(1)))]


def sort_by_value_and_index(arr):
    return [v for _, v in sorted(enumerate(arr, 1), key=prod)]
