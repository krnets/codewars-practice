# def decrypt(encrypted_text, n):
#     if n < 1:
#         return encrypted_text
#     chars = list(encrypted_text)
#     k = len(encrypted_text)
#     mid = k // 2
#     while n:
#         replacement = []
#         odd_indexed_chars = chars[:mid]
#         even_indexed_chars = chars[mid:]
#         for x, y in zip(even_indexed_chars, odd_indexed_chars):
#             replacement.append(x)
#             replacement.append(y)
#         if k & 1:
#             replacement.append(even_indexed_chars[-1])
#         chars = replacement
#         n -= 1
#     return "".join(chars)


# def encrypt(text, n):
#     if n < 1:
#         return text
#     chars = list(text)
#     while n:
#         odd_indexed_chars = [c for i, c in enumerate(chars) if i & 1]
#         even_indexed_chars = [c for i, c in enumerate(chars) if not i & 1]
#         chars = odd_indexed_chars + even_indexed_chars
#         n -= 1
#     return "".join(chars)


from itertools import zip_longest

def decrypt(encrypted_text, n):
    if n < 1:
        return encrypted_text
    mid = len(encrypted_text) // 2
    for _ in range(n):
        encrypted_text = "".join(b + a for a, b in zip_longest(encrypted_text[:mid], encrypted_text[mid:], fillvalue=""))
    return encrypted_text


def encrypt(text, n):
    for _ in range(n):
        text = text[1::2] + text[::2]
    return text
