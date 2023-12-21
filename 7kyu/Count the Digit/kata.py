# def nb_dig(n, d):
#     digit = str(d)
#     return sum(str(i * i).count(digit) for i in range(n + 1))


# def nb_dig(n, d):
#     return "".join(map(lambda i: str(i * i), range(n + 1))).count(str(d))


def nb_dig(n, d):
    return "".join(str(i * i) for i in range(n + 1)).count(str(d))
