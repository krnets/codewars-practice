def decode(strng):
    return strng.translate(str.maketrans("0123456789", "5987604321"))
