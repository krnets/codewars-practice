from itertools import repeat

# def count_arara(n):
#     res = " ".join(repeat("adak", n // 2))
#     return (res + " anane").lstrip() if n & 1 else res


# def count_arara(n):
#     return " ".join(["adak"] * (n // 2) + ["anane"] * (n & 1))


# def count_arara(n):
#     q, r = divmod(n, 2)
#     return " ".join(["adak"] * q + ["anane"] * r)


# def count_arara(n):
#     return (" ".join(repeat("adak", n // 2)) + " anane" * (n & 1)).lstrip()


def count_arara(n):
    return (" ".join(repeat("adak", n >> 1)) + " anane" * (n & 1)).lstrip()
