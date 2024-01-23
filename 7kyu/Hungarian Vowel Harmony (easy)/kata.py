# front_vowel = set("e é i í ö ő ü ű".split())
# back_vowel = set("a á o ó u ú".split())


# def dative(word):
#     for c in reversed(word):
#         if c in front_vowel: return word + "nek"
#         if c in back_vowel: return word + "nak"


hu_suffix = dict(dict.fromkeys("eéiíöőüű", "nek"), **dict.fromkeys("aáoóuú", "nak"))

def dative(word):
    return word + next(hu_suffix[c] for c in reversed(word) if c in hu_suffix)
