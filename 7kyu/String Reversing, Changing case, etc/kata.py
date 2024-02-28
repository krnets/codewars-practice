def reverse_and_mirror(s1, s2):
    return s2[::-1].swapcase() + "@" * 3 + s1[::-1].swapcase() + s1.swapcase()
