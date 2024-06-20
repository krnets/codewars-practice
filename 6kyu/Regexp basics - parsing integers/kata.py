import re


# def to_integer(string):
#     if re.fullmatch(r"-?0b[10]+", string):
#         return int(string, 2)
#     if re.fullmatch(r"-?0o[0-7]+", string):
#         return int(string, 8)
#     if re.fullmatch(r"-?0x[\dA-Fa-f]+", string):
#         return int(string, 16)
#     if re.fullmatch(r"[+-]?\d+", string):
#         return int(string)
#     return None


def to_integer(string):
    binary = "0b[10]+"
    octal = "0o[0-7]+"
    hexadecimal = "0x[\dA-Fa-f]+"
    pattern = ("{}" * 5).format("[+-]?", "(", "\d+|", "|".join([binary, octal, hexadecimal]), ")")
    return int(string, (0, 10)[string[1:].isdigit()]) if re.fullmatch(pattern, string) else None