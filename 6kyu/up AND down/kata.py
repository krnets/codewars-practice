def arrange(strng):
    words = strng.split()

    for i in range(1, len(words)):
        if len(words[i - (i % 2)]) > len(words[i + (i % 2) - 1]):
            words[i], words[i - 1] = words[i - 1], words[i]

    return " ".join((str.lower, str.upper)[i & 1](word) for i, word in enumerate(words))
