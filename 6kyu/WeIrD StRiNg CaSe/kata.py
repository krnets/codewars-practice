# def to_weird_case(words):
#     return " ".join("".join(c.lower() if i & 1 else c.upper() for i, c in enumerate(word)) for word in words.split())


def to_weird_case(words):
    return " ".join(map(to_weird_case_word, words.split()))


# def to_weird_case_word(word):
#     return "".join(c.lower() if i & 1 else c.upper() for i, c in enumerate(word))


def to_weird_case_word(word):
    return "".join((c.upper(), c.lower())[i & 1] for i, c in enumerate(word))
