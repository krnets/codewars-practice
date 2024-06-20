# def read_zalgo(zalgotext):
#     return "".join(c for c in zalgotext if ord(c) < 128)


# def read_zalgo(zalgotext):
#     return "".join(filter(str.isascii, zalgotext))


def read_zalgo(zalgotext: str):
    return zalgotext.encode("ASCII", errors="ignore").decode()
