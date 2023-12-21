# def vert_mirror(strng):
#     return "\n".join(s[::-1] for s in strng.split("\n"))

# def hor_mirror(strng):
#     return "\n".join(strng.split("\n")[::-1])

# def oper(fct, s):
#     return fct(s)


def vert_mirror(strng):
    return "\n".join(s[::-1] for s in strng)

def hor_mirror(strng):
    return "\n".join(strng[::-1])

def oper(fct, s):
    return fct(s.split("\n"))
