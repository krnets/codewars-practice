def gcdi(x, y):
    return abs(x) if not y else gcdi(y, x % y)


def lcmu(a, b):
    return abs(a * b) // gcdi(a, b)


def som(a, b):
    return a + b


def maxi(a, b):
    return a if a > b else b


def mini(a, b):
    return a if a < b else b


# def oper_array(fct, arr, init):
#     out = []
#     prev = init
#     for x in arr:
#         out.append(fct(prev, x))
#         prev = out[-1]
#     return out


def oper_array(fct, arr, init):
    out, num = [], init
    for x in arr:
        num = fct(num, x)
        out.append(num)
    return out
