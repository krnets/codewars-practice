def sp_eng(sentence):
    match_word = "english"
    j = 0

    for c in sentence.lower():
        if c == match_word[j]:
            j += 1
            if j == len(match_word):
                return True

    return False


# def sp_eng(sentence):
#     return 'english' in sentence.lower()
