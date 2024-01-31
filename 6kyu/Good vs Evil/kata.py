def good_vs_evil(good, evil):
    good_worth = [1, 2, 3, 3, 4, 10]
    evil_worth = [1, 2, 2, 2, 3, 5, 10]
    good_score = sum(x * int(y) for x, y in zip(good_worth, good.split()))
    evil_score = sum(x * int(y) for x, y in zip(evil_worth, evil.split()))

    return "Battle Result: " + (
        "Evil eradicates all trace of Good" if evil_score > good_score
        else "Good triumphs over Evil" if good_score > evil_score
        else "No victor on this battle field")
