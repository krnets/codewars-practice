import re


def time_correct(t):
    if not t:
        return t
    if not re.fullmatch(r"\d{2}:\d{2}:\d{2}", t):
        return None
    hours, minutes, seconds = map(int, t.split(":"))
    if seconds > 59:
        seconds = seconds % 60
        minutes += 1
    if minutes > 59:
        minutes = minutes % 60
        hours += 1
    hours = hours % 24
    return "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
