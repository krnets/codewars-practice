from collections import Counter


# def find_children(dancing_brigade):
#     freq = Counter(dancing_brigade)
#     res = ""
#     for c in sorted(filter(str.isupper, freq.keys())):
#         res += c
#         res += c.lower() * freq[c.lower()]
#     return res


# def find_children(dancing_brigade):
#     return "".join(sorted(dancing_brigade, key=lambda c: (c.upper(), c.islower())))


# def find_children(dancing_brigade):
#     return "".join(sorted(dancing_brigade, key=lambda c: (c.upper(), c)))


def find_children(dancing_brigade):
    return "".join(sorted(dancing_brigade, key=lambda c: (c.lower(), c)))
