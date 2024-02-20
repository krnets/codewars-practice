def generate_hashtag(s) -> str or bool:
    res = "#" + s.title().replace(" ", "")
    return (res, False)[not s or len(res) > 140]
