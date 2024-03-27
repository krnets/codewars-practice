from itertools import chain

def cant_beat_so_join(numbers):
    return [*chain.from_iterable(sorted(numbers, key=sum, reverse=True))]


# def cant_beat_so_join(numbers):
#     return sum(sorted(numbers, key=sum, reverse=True), [])
