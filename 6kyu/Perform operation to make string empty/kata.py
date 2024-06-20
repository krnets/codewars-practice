from collections import Counter


def last_non_empty_string(strng: str) -> str:
    freq = Counter(strng)
    m = max(freq.values()) - 1
    for k in freq.keys():
        strng = strng.replace(k, "", m)
    return strng
