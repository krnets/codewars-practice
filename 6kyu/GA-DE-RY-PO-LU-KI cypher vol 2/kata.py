# def encode(message, _key):
#     G, A = "", ""
#     for i, c in enumerate(_key.upper()):
#         if i % 2 == 0:
#             G += c
#         else:
#             A += c
#     G += G.lower()
#     A += A.lower()
#     return message.translate(str.maketrans(G + A, A + G))


def encode(message, _key):
    G, A = "", ""
    for i, c in enumerate(_key.upper() + _key.lower()):
        if i & 1: A += c
        else:     G += c
    return message.translate(str.maketrans(G + A, A + G))

decode = encode
