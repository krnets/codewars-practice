# def endless_string(seq: str, start: int, length: int) -> str:
#     if length < 0:
#         start += length + 1
#         length *= -1
#     return (seq[start % len(seq) :] + seq * length)[:length]

from itertools import cycle, islice


# def endless_string(seq: str, start: int, length: int) -> str:
#     i = ((length + 1) * (length < 0) + start) % len(seq)
#     return "".join(islice(cycle(seq), i, i + abs(length)))


def endless_string(seq: str, start: int, length: int) -> str:
    i = min(start, start + length) % len(seq) + (length < 0)
    j = i + abs(length)
    return "".join(islice(cycle(seq), i, j))
