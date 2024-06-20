# def play_pass(s, n):
#     chars = list(s.upper())
#     offset = ord("A")
#     for i, c in enumerate(chars):
#         if c.isalpha():
#             chars[i] = chr((ord(c) + n + offset) % 26 + offset)
#             if i & 1:
#                 chars[i] = chars[i].lower()
#         elif c.isnumeric():
#             chars[i] = str(abs(int(c) - 9))
#     return "".join(reversed(chars))

from string import digits, ascii_uppercase as abc


def play_pass(s, n):
    encoded = s.translate(str.maketrans(abc + digits, abc[n:] + abc[:n] + digits[::-1]))
    return "".join(reversed([c.lower() if i & 1 else c for i, c in enumerate(encoded)]))
