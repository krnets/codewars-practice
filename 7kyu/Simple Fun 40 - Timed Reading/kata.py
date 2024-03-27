import re

# def timed_reading(max_length, text):
#     matches = re.findall(r"\b\w+\b", text)
#     return len([*filter(lambda m: len(m) <= max_length, matches)])


# def timed_reading(max_length, text):
#     return sum(len(m) <= max_length for m in re.findall(r"\w+", text))


def timed_reading(max_length, text):
    return len(re.findall(r"\b(\w{{1,{max_len}}})\b".format(max_len=max_length), text))
