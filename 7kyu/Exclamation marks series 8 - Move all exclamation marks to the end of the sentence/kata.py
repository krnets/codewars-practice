def remove(string: str) -> str:
    return string.replace("!", "") + "!" * string.count("!")
