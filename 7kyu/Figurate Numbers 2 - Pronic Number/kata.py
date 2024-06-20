# def is_pronic(n):
#     if n < 0:
#         return False
#     p = int(n**0.5) - 1
#     return p * (p + 1) == n or (p + 1) * (p + 2) == n


def is_pronic(n):
    return n >= 0 and (p := int(n**0.5)) * (p + 1) == n
