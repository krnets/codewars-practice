from itertools import zip_longest


def split_and_add(numbers, n):
    for _ in range(n):
        mid = len(numbers) // 2
        left, right = numbers[:mid], numbers[mid:]
        numbers = [*map(sum, zip_longest(*map(reversed, [left, right]), fillvalue=0))][::-1]
    return numbers

