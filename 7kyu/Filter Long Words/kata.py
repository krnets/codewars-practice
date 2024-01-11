# def filter_long_words(sentence, n):
#     return [word for word in sentence.split() if len(word) > n]

import re


def filter_long_words(sentence, n):
    # return re.findall("[A-Za-z_\(\)]{%s,}" % str(n + 1), sentence)
    # return re.findall("[\w_\(\)]{%s,}" % str(n + 1), sentence)
    return re.findall("[^\s]{%s,}" % str(n + 1), sentence)
