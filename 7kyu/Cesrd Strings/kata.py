# def uncensor(infected, discovered):
#     chars = list(infected)
#     j = 0
#     for i, c in enumerate(chars):
#         if c == "*":
#             chars[i] = discovered[j]
#             j += 1
#     return "".join(chars)


def uncensor(infected, discovered):
    it = iter(discovered)
    return "".join(next(it) if c == "*" else c for c in infected)
