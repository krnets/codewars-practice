from itertools import chain


def well(arr):
    n = sum(idea.lower() == "good" for idea in chain.from_iterable(arr) if isinstance(idea, str))
    return ("Fail!", "Publish!", "I smell a series!")[(n > 0) +  (n > 2)]

    # return "I smell a series!" if n > 2 else "Publish!" if n > 0 else "Fail!"
