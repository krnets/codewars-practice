# def decode_pass(pass_list, bits):
#     s = "".join(chr(int(b, 2)) for b in bits.split())
#     for pwd in pass_list:
#         if pwd == s:
#             return pwd
#     return False


# def decode_pass(pass_list, bits):
#     s = "".join(chr(int(b, 2)) for b in bits.split())
#     return next((pwd for pwd in pass_list if pwd == s), False)


def decode_pass(pass_list, bits):
    s = "".join(chr(int(b, 2)) for b in bits.split())
    return s if s in pass_list else False
