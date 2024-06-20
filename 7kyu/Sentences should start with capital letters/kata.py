# def fix(paragraph):
#     if not paragraph:
#         return paragraph

#     sentences = paragraph.split(". ")

#     for i, sentence in enumerate(sentences):
#         sentences[i] = sentence[0].upper() + sentence[1:]

#     return ". ".join(sentences)


# def fix(paragraph):
#     return ". ".join(map(str.capitalize, paragraph.split(". ")))

import re


# def fix(paragraph):
#     return re.sub(r"(^|\. )\w", lambda m: m[0].upper(), paragraph)


def fix(paragraph):
    return re.sub(r"(^|\. )\w", lambda m: m.group().upper(), paragraph)
