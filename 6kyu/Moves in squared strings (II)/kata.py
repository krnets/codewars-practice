def rot(strng):
    return strng[::-1]


# def selfie_and_rot(strng):
#     splits = [line + "." * len(line) for line in strng.splitlines()]
#     return "\n".join(splits) + "\n" + "\n".join("".join(reversed(w)) for w in reversed(splits))


def selfie_and_rot(strng):
    s_dot = "\n".join(line + "." * len(line) for line in strng.splitlines())
    return s_dot + "\n" + rot(s_dot)


def oper(fct, s):
    return fct(s)
