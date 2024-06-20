import re


def heggeleggleggo(word):
    return "".join(re.sub(r"([^aeiou\s])", r"\1egg", word, flags=re.I))
