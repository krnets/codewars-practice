import re

def to_camel_case(text):
    words = re.split(r"[-_]", text)
    return words[0] + "".join(map(str.title, words[1:]))
