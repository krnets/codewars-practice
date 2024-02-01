# def wave(people):
#     res = []
#     chars = list(people)
#     for i, c in enumerate(people):
#         if c != " ":
#             chars[i] = chars[i].upper()
#             res.append("".join(chars))
#             chars[i] = chars[i].lower()
#     return res


def wave(people):
    return [people[:i] + c.upper() + people[i + 1 :] for i, c in enumerate(people) if c.isalpha()]
