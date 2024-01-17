# def pattern(n):
#     arr = []
#     for i in range(n)
#         s = "1"
#         s += "*" * i
#         s += str(i + 1) if i else ""
#         arr.append(s)
#     return "\n".join(arr)


# 1
# 1*2
# 1**3
# 1***4
# 1****5
# 1*****6
# 1******7


def pattern(n):
    return "\n1".join("*" * i + str(i + 1) for i in range(n))
