# def pattern(n):
#     if n < 1:
#         return ""
#     lines = []
#     for i in range(n, -1, -1):
#         sub = ""
#         for j in range(n, i, -1):
#             sub += str(j)
#         lines.append(sub)

#     return "\n".join(reversed(lines)).rstrip()


def pattern(n):
    return "\n".join("".join(str(j) for j in range(n, i, -1)) for i in range(n))
