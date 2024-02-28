# def multiply_and_filter(seq, multiplier):
#     return [
#         x * multiplier
#         for x in seq
#         if isinstance(x, (int, float)) and not isinstance(x, bool)
#     ]


def multiply_and_filter(seq, multiplier):
    return [x * multiplier for x in seq if type(x) in (int, float)]
