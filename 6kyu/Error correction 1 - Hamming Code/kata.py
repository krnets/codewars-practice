def encode(string):
    return "".join(b * 3 for c in string for b in f"{ord(c):08b}")


def decode(bits):
    splits = "".join("0" if bits[i : i + 3].count("0") > 1 else "1" for i in range(0, len(bits), 3))
    return "".join(chr(int(splits[i : i + 8], 2)) for i in range(0, len(splits), 8))