def zebulans_nightmare(function):
    words = function.split("_")

    for i in range(1, len(words)):
        words[i] = words[i].title()

    return "".join(words)
