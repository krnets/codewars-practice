# def binary_to_string(binary):
#     return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))


from textwrap import wrap


def binary_to_string(binary):
    return "".join(chr(int(w, 2)) for w in wrap(binary, 8))
