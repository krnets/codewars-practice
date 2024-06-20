import re


# def pig_it(text):
#     return re.sub(r"\w+", lambda m: m.group()[1:] + m.group()[0] + "ay", text)


def pig_it(text):
    return re.sub(r"([a-z])([a-z]*)", r"\2\1ay", text, flags=re.I)
