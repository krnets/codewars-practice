# def binary_to_string(binary):
#     chars = binary.split("0b")
#     return "".join(chr(int(c, 2)) for c in chars[1:])


# def binary_to_string(binary):
#     return "".join(map(chr, (int(c, 2) for c in binary[2:].split("0b"))))


def binary_to_string(binary):
    codes = binary[2:].split("0b")
    return bytes(int(c, 2) for c in codes).decode("ascii")
