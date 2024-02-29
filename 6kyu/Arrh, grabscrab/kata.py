def grabscrab(said, possible_words):
    return [*filter(lambda w: sorted(w) == sorted(said), possible_words)]
