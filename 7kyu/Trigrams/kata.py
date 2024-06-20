# def trigrams(phrase):
#     n = 3
#     if len(phrase) < n:
#         return ""
#     phrase = phrase.replace(" ", "_")
#     return " ".join(phrase[i : i + n] for i in range(len(phrase) - n + 1))


def trigrams(phrase):
    n = 3
    if len(phrase) < n:
        return ""
    phrase = phrase.replace(" ", "_")
    columns = [phrase[i:] for i in range(n)]
    return " ".join(map("".join, zip(*columns)))
