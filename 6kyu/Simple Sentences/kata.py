# def make_sentences(parts):
#     res = parts[0] + " "

#     for x in parts[1:]:
#         if x == ".": continue
#         if x == ",": res = res[:-1] + x + " "
#         else: res += x + " "
#     return res[:-1] + "."


# def make_sentences(parts):
#     return " ".join(parts).replace(" ,", ",").rstrip(" .") + "."

import re

def make_sentences(parts):
    return re.sub(r" (?=[.,])", "", " ".join(parts)).rstrip(".") + "."
