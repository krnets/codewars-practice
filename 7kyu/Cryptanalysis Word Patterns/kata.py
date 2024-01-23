# def word_pattern(word):
#     word = word.lower()
#     letters = list(dict.fromkeys(word).keys())
#     return '.'.join(str(letters.index(c)) for c in word)


def word_pattern(word):
    word = word.lower()
    d = {k: str(i) for i, k in enumerate(dict.fromkeys(word))}
    return ".".join(map(d.get, word))
