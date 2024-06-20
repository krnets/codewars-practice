from string import ascii_lowercase as abc, ascii_uppercase as ABC

# def next_letter(s):
#     table = str.maketrans(abc + ABC, abc[1:] + abc[0] + ABC[1:] + ABC[0])
#     return s.translate(table)


def next_letter(s):
    return "".join(chr(ord(c) + (1, -25)[c in "Zz"]) if c.isalpha() else c for c in s)
