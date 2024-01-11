# def trim(phrase, size):
#     if len(phrase) <= size:
#         return phrase
#     if size > 3:
#         return phrase[: size - 3] + "..."
#     return phrase[:size] + "..."


def trim(phrase, size):
    n = len(phrase)
    i = size - 3 * (3 < size < n)
    return phrase[:i] + "..." * (n > size)
