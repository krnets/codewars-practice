# def hidden(num):
#     maya_key = "oblietadnm"
#     res = []

#     while num:
#         num, i = divmod(num, 10)
#         res += maya_key[i]
#     return "".join(reversed(res))


def hidden(num):
    maya_key = "oblietadnm"
    return str(num).translate(str.maketrans("".join(map(str, range(10))), maya_key))
