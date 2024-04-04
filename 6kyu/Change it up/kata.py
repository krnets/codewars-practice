# def changer(s):
#     offset_a, offset_A, res = ord("a") - 1, ord("A") - 1, ""

#     for c in s:
#         if c.isalpha():
#             if c.isupper(): d = chr((ord(c) - offset_A) % 26 + 1 + offset_A)
#             else:           d = chr((ord(c) - offset_a) % 26 + 1 + offset_a)
#             if d.lower() in "aeiou": res += d.upper()
#             else:                    res += d.lower()
#         else:
#             res += c
#     return res

from string import ascii_lowercase as abc


def changer(s):
    vowels_idx = [(i - 1) % 26 for i, c in enumerate(abc) if c in "aeiou"]
    bcd = abc[1:] + abc[0]
    bcd_mixed = "".join(c.upper() if i in vowels_idx else c for i, c in enumerate(bcd))

    return s.lower().translate(str.maketrans(abc, bcd_mixed))
