# def to_binary(n):
#     return format(n & 0xFFFFFFFF, "b")


def to_binary(n):
    return f"{n & 0xFFFFFFFF:b}"
