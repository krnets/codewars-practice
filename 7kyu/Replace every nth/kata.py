# def replace_nth(text, n, old_value, new_value):
#     if n < 1:
#         return text
#     chars = list(text)
#     m = 0
#     for i, c in enumerate(chars):
#         if c == old_value:
#             m += 1
#             if m == n:
#                 chars[i] = new_value
#                 m = 0
#     return "".join(chars)


def replace_nth(text, n, old_value, new_value):
    if n < 1:
        return text
    chars = list(text)
    m = 0
    for i, c in enumerate(chars):
        if c == old_value:
            m += 1
            if m % n == 0:
                chars[i] = new_value
    return "".join(chars)
