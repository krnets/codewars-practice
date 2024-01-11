from bisect import bisect
from itertools import accumulate, takewhile


# def minimum_steps(numbers, value):
#     return len([*takewhile(lambda sum: sum < value, accumulate(sorted(numbers)))])


def minimum_steps(numbers, value):
    # return bisect(list(accumulate(sorted(numbers))), value - 1)
    return bisect([*accumulate(sorted(numbers))], value - 1)
