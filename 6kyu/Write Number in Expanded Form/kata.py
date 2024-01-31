# def expanded_form(num):
#     m = 1
#     expansion = []
#     while num:
#         expansion.append(num % 10 * m)
#         m *= 10
#         num //= 10
#     return ' + '.join(x for x in map(str, reversed(expansion)) if x != '0')


# def expanded_form(num):
#     digits = str(num)
#     return " + ".join(x + "0" * (len(digits) - i) for i, x in enumerate(digits, 1) if x != "0")


def expanded_form(num):
    digits = str(num)
    return " + ".join(x.ljust(len(digits) - i, "0") for i, x in enumerate(digits) if x != "0")
