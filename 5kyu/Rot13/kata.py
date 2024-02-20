# from string import ascii_lowercase as abc_lo, ascii_uppercase as abc_up

# cipher_lo = str.maketrans(abc_lo, abc_lo[13:] + abc_lo[:13])
# cipher_up = str.maketrans(abc_up, abc_up[13:] + abc_up[:13])

# def rot13(message: str):
#     return message.translate(cipher_lo).translate(cipher_up)


# from string import ascii_lowercase as abc_lo, ascii_uppercase as abc_up

# cipher = str.maketrans(abc_lo + abc_up, abc_lo[13:] + abc_lo[:13] + abc_up[13:] + abc_up[:13])

# rot13 = lambda message: message.translate(cipher)


from codecs import encode


def rot13(message: str):
    return encode(message, "rot13")
