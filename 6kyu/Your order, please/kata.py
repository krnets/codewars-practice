import re


def order(sentence):
    tuples = [(int(re.sub(r"[^\d]", "", w)), w) for w in sentence.split()]
    return " ".join(w for _, w in sorted(tuples))
