def solve(a, b):
    return sum(map(is_upside_down, range(a, b)))


# def is_upside_down(num):
#     if num < 10:
#         return num in (0, 1, 8)
#     return (s := str(num))[::-1] == s.translate(str.maketrans("2345679", "----9-6"))


def is_upside_down(num):
    if num < 10:
        return num in (0, 1, 8)
    m = num
    while m:
        m, r = divmod(m, 10)
        if r in (2, 3, 4, 5, 7):
            return False
    return (s := str(num))[::-1] == s.translate(str.maketrans("69", "96"))


# def is_upside_down(num):
#     if num < 10:
#         return num in (0, 1, 8)
#     d = {6: 9, 9: 6}
#     digits, opposite = [], []
#     while num:
#         num, r = divmod(num, 10)
#         if r in (2, 3, 4, 5, 7):
#             return False
#         digits.append(r)
#         opposite.append(d.get(r, r))
#     return digits[::-1] == opposite
