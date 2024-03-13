def gaslighting(shirt_word: str, your_word: str, friends_letters: str) -> bool:
    return any(
        letter in friends_letters
        for shirt_c, your_c in zip(shirt_word, your_word)
        for letter in (shirt_c, your_c)
        if shirt_c != your_c
    )
