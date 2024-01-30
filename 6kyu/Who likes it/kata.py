# def likes(names):
#     if len(names) > 3:
#         return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
#     elif len(names) == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     elif len(names) == 2:
#         return f"{names[0]} and {names[1]} like this"
#     elif len(names) == 1:
#         return f"{names[0]} likes this"
#     return "no one likes this"


# def likes(names):
#     return {
#         0: "no one likes this",
#         1: "{} likes this",
#         2: "{} and {} like this",
#         3: "{}, {} and {} like this",
#         4: "{}, {} and {others} others like this",
#     }[min(4, n := len(names))].format(*names[:3], others=n - 2)


def likes(names):
    match names:
        case []:            return "no one likes this"
        case [a]:           return f"{a} likes this"
        case [a, b]:        return f"{a} and {b} like this"
        case [a, b, c]:     return f"{a}, {b} and {c} like this"
        case [a, b, *rest]: return f"{a}, {b} and {len(rest)} others like this"
