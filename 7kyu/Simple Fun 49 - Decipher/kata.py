# def decipher(cipher):
#     i = 0
#     ans = ""
#     while i < len(cipher):
#         if cipher[i] == "1":
#             ans += chr(int(cipher[i : i + 3]))
#             i += 3
#         else:
#             ans += chr(int(cipher[i : i + 2]))
#             i += 2
#     return ans

import re

def decipher(cipher):
    return re.sub(r"1?\d\d", lambda m: chr(int(m.group())), cipher)
