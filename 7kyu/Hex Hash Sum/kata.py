# def hex_hash(code):
#     hex_ascii_joined = "".join(f"{ord(c):x}" for c in code)
#     return sum(map(int, filter(str.isdigit, hex_ascii_joined)))


def hex_hash(code: str) -> int:
    return sum(map(int, filter(str.isdigit, code.encode().hex())))
