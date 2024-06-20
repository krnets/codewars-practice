# def rot_90_clock(strng):
#     return "\n".join(diag_1_sym(strng).split("\n")[::-1])[::-1]


def rot_90_clock(strng):
    return "\n".join("".join(x) for x in zip(*strng.split("\n")[::-1]))


def diag_1_sym(strng):
    return "\n".join("".join(row) for row in zip(*strng.split("\n")))


# def selfie_and_diag1(strng):
#     diag = diag_1_sym(strng).split("\n")
#     return "\n".join(x + "|" + diag[i] for i, x in enumerate(strng.split("\n")))


def selfie_and_diag1(strng):
    return "\n".join(
        "|".join(x) for x in zip(strng.split("\n"), diag_1_sym(strng).split("\n"))
    )


def oper(fct, s):
    return fct(s)


# rot_90_clock = lambda strng: zip(*strng[::-1])
# diag_1_sym = lambda strng: zip(*strng)
# selfie_and_diag1 = lambda strng: (tuple(l + "|") + r for l, r in zip(strng, diag_1_sym(strng)))
# oper = lambda fct, s: "\n".join(map("".join, fct(s.split("\n"))))
