# def reverse(a):
#     s = "".join(a)[::-1]
#     i, res = 0, []
#     for w in a:
#         res.append(s[i : i + len(w)])
#         i += len(w)
#     return res


def reverse(a):
    s = iter(reversed("".join(a)))
    return ["".join(next(s) for _ in w) for w in a]
