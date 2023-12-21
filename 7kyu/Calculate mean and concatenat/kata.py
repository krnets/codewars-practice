# def mean(lst):
#     nums = [*map(int, filter(lambda x: x.isdigit(), lst))]
#     strings = "".join(filter(lambda x: not x.isdigit(), lst))
#     return [sum(nums) / len(nums), strings]


# def mean(lst):
#     nums = [*map(int, filter(str.isnumeric, lst))]
#     letters = "".join(filter(str.isalpha, lst))
#     return [sum(nums) / len(nums), letters]

import statistics


def mean(lst):
    nums = [*map(int, filter(str.isnumeric, lst))]
    letters = "".join(filter(str.isalpha, lst))
    return [statistics.mean(nums), letters]
