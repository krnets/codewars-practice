from math import log10


# def print_nums(*args):
#     if not args:
#         return ""
#     width = int(log10(max(args))) + 1
#     return "\n".join(f"{x:0{width}}" for x in args)


def print_nums(*args):
    if not args:
        return ""
    width = len(str(max(args)))
    return "\n".join(str(x).zfill(width) for x in args)
