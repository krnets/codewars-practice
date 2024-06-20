# def mirror(text):
#     words = text[::-1].split()[::-1]
#     length = max(len(w) for w in words)
#     stars = "*" * (length + 4)

#     for i, w in enumerate(words):
#         words[i] = "* " + w.ljust(length) + " *"

#     words.insert(0, stars)
#     words.append(stars)

#     return "\n".join(words)


def mirror(text):
    words = [word[::-1] for word in text.split()]
    length = max(map(len, words))
    stars = ["*" * (length + 4)]
    for i, word in enumerate(words):
        words[i] = "* {} *".format(word.ljust(length))
    return "\n".join(stars + words + stars)
