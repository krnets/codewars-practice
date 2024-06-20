# def re_ordering(text):
#     words = text.split()
#     pos = next(i for i, word in enumerate(words) if word[0].isupper())
#     arr = [words[pos]] + words[:pos] + words[pos + 1 :]
#     return " ".join(arr)


def re_ordering(text):
    return " ".join(sorted(text.split(), key=str.islower))
