import re


def to_seconds(time):
    if not re.fullmatch(r"\d{2}:[0-5]\d:[0-5]\d", time):
        return None

    hh, mm, ss = map(int, time.split(":"))
    return hh * 60 * 60 + mm * 60 + ss
