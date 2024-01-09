def remove_consecutive_duplicates(s: str) -> str:
    words = []
    for word in s.split():
        if words and words[-1] == word:
            continue
        else:
            words.append(word)
    return " ".join(words)
