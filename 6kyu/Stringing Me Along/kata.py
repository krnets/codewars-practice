from functools import partial

def create_message(s="", words=[]):
    return partial(create_message, words=words + [s]) if s else " ".join(words)
