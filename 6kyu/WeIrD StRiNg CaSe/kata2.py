def to_weird_case(words):
    return " ".join(
        "".join((c.upper, c.lower)[i & 1]() for i, c in enumerate(word))
        for word in words.split()
    )
