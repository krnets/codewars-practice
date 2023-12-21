# from string import ascii_lowercase as abc

# def add_letters(*letters):
#     offset = ord("a") - 1
#     letters_sum = sum(ord(c) - offset for c in letters)
#     return ("z" + abc)[letters_sum % 26]

# def add_letters(*letters):
# return ('z', *)


def add_letters(*letters):
    lookup = ["z"] + [*map(chr, range(ord("a"), ord("z")))]
    offset = ord("a") - 1
    letters_sum = sum(ord(c) - offset for c in letters)
    return lookup[letters_sum % 26]
