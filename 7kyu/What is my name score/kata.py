alpha = {"ABCDE": 1, "FGHIJ": 2, "KLMNO": 3, "PQRST": 4, "UVWXY": 5}

# from preloaded import alpha


def name_score(name):
    score = 0
    for c in name.upper():
        for k, v in alpha.items():
            if c in k:
                score += v
                break
    return {name: score}
