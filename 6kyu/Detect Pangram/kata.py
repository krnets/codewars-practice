from string import ascii_lowercase

# def is_pangram(s):
#     return sorted(set(c for c in s.lower() if c.isalpha())) == list(ascii_lowercase)


def is_pangram(s):
    return set(ascii_lowercase).issubset(s.lower())
