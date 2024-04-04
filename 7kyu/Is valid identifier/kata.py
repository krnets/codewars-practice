import re

# def is_valid(idn):
#     return bool(idn and re.fullmatch(r"[A-Za-z_$][A-Za-z\d_$]*", idn))


# def is_valid(idn):
#     return bool(re.fullmatch(r"[a-z_$][\w$]*", idn, re.I))


def is_valid(idn):
    return idn.replace("$", "d").isidentifier()
