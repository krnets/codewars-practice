import re

# def autocomplete(input_, dictionary):
#     input_ = "".join(filter(str.isalpha, input_))
#     return [*filter(lambda w: w.lower().startswith(input_), dictionary)][:5]


def autocomplete(input_, dictionary):
    input_ = "".join(filter(str.isalpha, input_))
    starts_with = lambda w: re.match("^" + input_, w, re.I)
    return [*filter(starts_with, dictionary)][:5]
