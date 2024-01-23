import re


# def count_consonants(text):
# return len(set(re.sub(r"[^a-z]|[aeiou]", "", text.lower())))

from string import ascii_lowercase as alphabet

# def count_consonants(text):
#     return len((set(alphabet) ^ set("aeiou")) & set(text.lower()))


def count_consonants(text):
    return len(set(alphabet).difference("aeiou").intersection(text.lower()))
