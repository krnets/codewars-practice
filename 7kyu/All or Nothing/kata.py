def possibly_perfect(key, answers):
    return all(k != a for k, a in zip(key, answers)) or \
        not any(k != a for k, a in zip(key, answers) if k != "_")

