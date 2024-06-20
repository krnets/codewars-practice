# def find_missing_number(numbers):
#     n = len(numbers) + 1
#     return n * (n + 1) // 2 - sum(numbers)

# from itertools import count

# def find_missing_number(numbers):
#     nums_set = set(numbers)
#     return next(i for i in count(1) if i not in nums_set)


# def find_missing_number(numbers):
#     return sum(range(1, len(numbers) + 2)) - sum(numbers)


def find_missing_number(numbers):
    zeros = [0] * (len(numbers) + 2)
    zeros[0] = 1
    for num in numbers:
        zeros[num] = 1
    return zeros.index(0)
