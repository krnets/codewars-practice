from string import ascii_lowercase


def consonant_count(s):
    consonants = set(ascii_lowercase).difference("aeiou")
    return sum(c in consonants for c in s.lower())
